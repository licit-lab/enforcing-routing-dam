""" 
    Control algorithm
"""

import numpy as np
import networkx as nx
from scipy.sparse import csr_matrix
from scipy.linalg import block_diag
from itertools import repeat

# ======================================================================================================================
# Constants
# ======================================================================================================================


DEFAULT_MAP = {
    (0, 0): "Cpt_1",
    (0, 1): "Cpt_2",
    (0, 2): "Cpt_3",
    (1, 0): "Cpt_4",
    (1, 1): "Cpt_5",
    (1, 2): "Cpt_6",
    (2, 0): "Cpt_8",
    (2, 1): "Cpt_7",
    (2, 2): "Cpt_9",
}


DEFAULT_SPD = {
    "Cpt_1": 6.3,
    "Cpt_2": 6.3,
    "Cpt_3": 6.1,
    "Cpt_4": 6.4,
    "Cpt_5": 5.5,
    "Cpt_6": 5.4,
    "Cpt_8": 5.6,
    "Cpt_7": 5.2,
    "Cpt_9": 6.2,
}

SENSORS = (
    "Cpt_1",
    "Cpt_2",
    "Cpt_3",
    "Cpt_4",
    "Cpt_5",
    "Cpt_6",
    "Cpt_8",
    "Cpt_7",
    "Cpt_9",
)

TS = 180

# ======================================================================================================================
# Functions
# ======================================================================================================================


# Cooperative graph
def define_grid_graph(
    N: int = 3,
    M: int = 3,
    mapping: dict = DEFAULT_MAP,
    refSpeed: dict = DEFAULT_SPD,
    sensors: tuple = SENSORS,
    selfishness: float = 0.5,
) -> nx.Graph:
    """ Creates a grid graph for the control algorithm 
    
    :param N: row number, defaults to 3
    :type N: int, optional
    :param M: column number, defaults to 3
    :type M: int, optional
    :param mapping: mapping option to match symuvia, defaults to DEFAULT_MAP
    :type mapping: dict, optional
    :param refSpeed: Individual speed reference per zone 
    :type refSpeed: dict, optional
    :param selfishness: Weight for self control action cooperative action is then weighted as (1- selfishness)
    :type selfishness: dict, optional
    :return: tuple with 
    :rtype: tuple
    """

    # Creating cyclic  graph
    G = nx.grid_2d_graph(N, M)

    # Adding attributes to graph
    G.graph["self"] = selfishness

    # Relabeling nodes
    mapping = dict(zip(G.nodes(), sensors))

    # Explicit
    G = nx.relabel_nodes(G, mapping)

    # Set reference speed on node
    nx.set_node_attributes(G, refSpeed, "freeFlowSpeed")

    # Plot graph
    # nx.draw(G, node_color="#A0CBE2", with_labels=True)

    return G


def get_graph_data(G: nx.Graph) -> tuple:
    """ Get graph data 
    
    :param G: Undirected graph 
    :type G: nx.Graph
    :return: perron, laplacian, epsilon
    :rtype: tuple
    """

    L = nx.laplacian_matrix(G)
    D = dict(nx.degree(G))
    delta = D[max(D, key=D.get)]  # max degree
    epsilon = 1 / (10 * delta)

    N = len(G.nodes)
    P = np.identity(N) - epsilon * L

    A = nx.adjacency_matrix(G)

    return P, L, epsilon, A, D


class Integrator:
    def __init__(self, N: int = 1, SamplingTime: float = TS):
        self.N = N
        self.ix = np.zeros(N).reshape(1, N)
        self.x = np.zeros(N).reshape(1, N)
        self.T = SamplingTime
        self.t = [0]

    def integ(self, val: np.array) -> np.array:
        """
            Compute sum(T* x_k) and updates the memory 
        """
        area = self.T * val  # Base * height
        self.x = np.vstack((self.x, area))
        self.ix = np.vstack((self.ix, np.sum(self.x, axis=0)))
        self.time_update()
        return self.ix[-1]

    def time_update(self):
        """ time vector"""
        self.t.append(self.t[-1] + self.T)

    def __call__(self, val):
        """ Call like integ(error) """
        return self.integ(val)


class Derivator:
    def __init__(self, N: int = 1, SamplingTime: float = TS):
        self.N = N
        self.dx = np.zeros(N).reshape(1, N)
        self.x = np.zeros(N).reshape(1, N)  # For accessing the full vector
        self.T = SamplingTime
        self.t = [0]

    def diff(self, val):
        """
            Compute (x_k - x_{k-1})/T and updates the memory 
        """
        dif = (val - self.x[-1]) / self.T
        self.x = np.vstack((self.x, val))
        self.dx = np.vstack((self.dx, dif))
        self.time_update()
        return self.dx[-1]

    def time_update(self):
        """ time vector"""
        self.t.append(self.t[-1] + self.T)

    def __call__(self, val):
        """ Call like diff(error) """
        return self.diff(val)


class ComputeVanishingControl:
    """ 
        A class to compute control law
    """

    def __init__(self, G: nx.Graph, samplingTime: float = TS, dctPar: dict = {}, dfSpd: dict = {}) -> None:
        self.N = len(G.nodes)
        self.refSpeed = dfSpd

        # States
        self.integrator = Integrator(self.N, samplingTime)
        self.derivator = Derivator(self.N, samplingTime)
        self.derivatorCO = Derivator(self.N, samplingTime)
        self.windReset = np.zeros((1, self.N))

        # Boundaries
        self.uMax = 1
        self.uMin = 0

        # Control Parameters
        self.typeCtr = dctPar.get("CTR_ALG", "P")
        self.kP = dctPar.get("KP", 0.15)
        self.Ti = dctPar.get("TI", 1200)
        self.Td = dctPar.get("TD", 300)
        self.Twd = dctPar.get("TWD", 360)
        self.COkP = dctPar.get("COKP", 0.15)
        self.COTi = dctPar.get("COTI", 1200)
        self.COTd = dctPar.get("COTD", 300)
        self.COTwd = dctPar.get("COTWD", 360)
        self.beta = dctPar.get("BETA", 0.3)

        # Trigger
        self.trigger = dctPar.get("TRIGGER", -1)

        # Memory
        self.uKI = []
        self.localU = []
        self.coopU = []
        self.errorSignal = []
        self.U = []
        self.proportional = []

        self.ukP = []

    def __call__(self, simulationstep: int, triggertime: int, speeds: dict, G: nx.Graph) -> dict:
        """ Computes the control law based on current speeds and some graph information

            :param simulationstep: current simulation step
            :type simulationstep: int
            :param triggertime: trigger time on the control (ignored in automode)
            :type triggertime: int
            :param speeds: dict of region speeds
            :type speeds: dict
            :param G: Network graph
            :type G: nx.Graph
            :return: dictionary with vanishing policies per region
            :rtype: dict
        """

        # Case speed is empty
        if not speeds:
            return dict(zip(list(G.nodes), repeat(0)))

        self.zones = speeds[-1].keys()

        if self.typeCtr == "P":

            # Compute error
            errorState = np.array([self.refSpeed[s] - speeds[-1][s] for s in G.nodes])

            # Control
            control = self.kP * errorState

            # Memory Control
            self.errorSignal.append(errorState)
            self.localU.append(control)
            self.coopU.append(np.zeros(self.N))

            # Bound Control
            totalControl = np.clip(control, self.uMin, self.uMax)

        elif self.typeCtr == "PI":

            # Compute error
            errorState = np.array([self.refSpeed[s] - speeds[-1][s] for s in G.nodes])

            # Proportional
            proportional = self.kP * errorState

            # Integral
            integral = self.kP * 1 / self.Ti * self.integrator(errorState + self.windReset)

            # Control
            control = proportional + integral

            # Windup (update for next step)
            boundControl = np.clip(control, self.uMin, self.uMax)
            self.windReset = (boundControl - control) / self.Twd

            # Memory Control
            self.errorSignal.append(errorState)
            self.localU.append(control)
            self.coopU.append(np.zeros(self.N))

            # Bound Control
            totalControl = boundControl

        elif self.typeCtr == "PD":

            errorState = np.array([self.refSpeed[s] - speeds[-1][s] for s in G.nodes])

            # Proportional
            proportional = self.kP * errorState

            # Differential
            differential = self.kP * self.Td * self.derivator(errorState) * (errorState > -0.5)

            # Control
            control = proportional + differential

            # Memory Control
            self.errorSignal.append(errorState)
            self.localU.append(control)
            self.coopU.append(np.zeros(self.N))

            # Bound control
            totalControl = np.clip(control, self.uMin, self.uMax)

        elif self.typeCtr in ("COP", "COST1"):

            # Network data
            _, L, epsilon, _, _ = get_graph_data(G)  # Works because the graph is small

            # Normalized states
            normState = np.array([speeds[-1][s] / self.refSpeed[s] for s in G.nodes])

            # Compute local control
            localControl = np.clip(1 - normState, self.uMin, self.uMax)

            # Compute neighbor information
            proportional = self.kP * epsilon * L @ normState

            # Cooperative term
            neighControl = proportional

            # Memory control
            self.errorSignal.append(1 - normState)
            self.localU.append(localControl)
            self.coopU.append(neighControl)

            # Total control law
            totalControl = G.graph["self"] * localControl + (1 - G.graph["self"]) * np.clip(
                neighControl, self.uMin, self.uMax
            )

        elif self.typeCtr in ("COPI", "COST4"):

            # Network data
            _, L, epsilon, _, _ = get_graph_data(G)  # Works because the graph is small

            # Normalized states
            normState = np.array([speeds[-1][s] / self.refSpeed[s] for s in G.nodes])

            # Compute local control
            localControl = np.clip(1 - normState, self.uMin, self.uMax)

            # Compute neighbor information
            proportional = self.kP * epsilon * L @ normState
            integral = self.kP * 1 / self.Ti * epsilon * L * self.integrator(normState + self.windReset)

            # Cooperative term
            neighControl = proportional + integral
            boundControl = np.clip(neighControl, self.uMin, self.uMax)

            # Windup (update for next step)
            self.windReset = (boundControl - neighControl) / self.Twd

            # Memory control
            self.errorSignal.append(1 - normState)
            self.localU.append(localControl)
            self.coopU.append(neighControl)

            # Total control law
            totalControl = G.graph["self"] * localControl + (1 - G.graph["self"]) * np.clip(
                neighControl, self.uMin, self.uMax
            )

        elif self.typeCtr in ("COPE", "COST2", "COSTN1"):

            # Compute error
            errorState = np.array([self.refSpeed[s] - speeds[-1][s] for s in G.nodes])

            # Compute error normalized
            normError = np.array([(self.refSpeed[s] - speeds[-1][s]) / self.refSpeed[s] for s in G.nodes])

            # Proportional
            proportional = self.kP * errorState

            # Differential
            differential = self.kP * self.Td * self.derivator(errorState) * (errorState > -0.5)

            # Local Control
            localControl = np.clip(proportional + differential, self.uMin, self.uMax)

            # Network data
            _, L, epsilon, A, D = get_graph_data(G)  # Works because the graph is small
            d = np.array(list(D.values()))  # Find degrees vector

            # Cooperative term
            neighControl = np.clip(self.COkP * A / d @ np.maximum(normError, 0), self.uMin, self.uMax)
            neighControl = np.squeeze(np.asarray(neighControl))

            # Memory control
            self.errorSignal.append(normError)
            self.localU.append(localControl)
            self.coopU.append(neighControl)

            # Total control law
            totalControl = G.graph["self"] * localControl + (1 - G.graph["self"]) * neighControl

        elif self.typeCtr in ("COPEV2", "COST3", "COSTN2"):

            # Compute error
            errorState = np.array([self.refSpeed[s] - speeds[-1][s] for s in G.nodes])

            # Compute error normalized
            normError = np.array([(self.refSpeed[s] - speeds[-1][s]) / self.refSpeed[s] for s in G.nodes])

            # Proportional
            proportional = self.kP * errorState

            # Differential
            differential = self.kP * self.Td * self.derivator(errorState) * (errorState > -0.5)

            # Local Control
            localControl = np.clip(proportional + differential, self.uMin, self.uMax)

            # Network data
            A, d = self.computeActiveNeighbors(G, normError)

            # Cooperative term
            neighControl = np.clip(self.COkP * A / d[:, None] @ np.maximum(normError, 0), self.uMin, self.uMax)

            # Memory control
            self.errorSignal.append(normError)
            self.localU.append(localControl)
            self.coopU.append(neighControl)

            # Total control law
            totalControl = G.graph["self"] * localControl + (1 - G.graph["self"]) * neighControl

        elif self.typeCtr in ("COPNL", "COST3", "COSTN3"):

            # Compute error
            errorState = np.array([self.refSpeed[s] - speeds[-1][s] for s in G.nodes])

            # Compute error normalized
            normError = np.array([(self.refSpeed[s] - speeds[-1][s]) / self.refSpeed[s] for s in G.nodes])

            # Proportional
            proportional = self.kP * errorState

            # Differential
            differential = self.kP * self.Td * self.derivator(errorState) * (errorState > -0.5)

            # Local Control
            localControl = np.clip(proportional + differential, self.uMin, self.uMax)

            # Adjacency / Degree (Variable)
            A, d = self.computeActiveNeighbors(G, normError)

            # Cooperative (epsilon)
            neighControl = self.beta * (np.maximum(normError, 0) - A / d[:, None] @ np.maximum(normError, 0))

            # Memory control
            self.errorSignal.append(normError)
            self.localU.append(localControl)
            self.coopU.append(neighControl)

            # Total control law
            totalControl = (1 + neighControl) * localControl

            # Bounding control
            totalControl = np.clip(totalControl, self.uMin, self.uMax)

        elif self.typeCtr in ("COPD1", "COST5", "COSTN4"):

            # Compute error
            errorState = np.array([self.refSpeed[s] - speeds[-1][s] for s in G.nodes])

            # Normalized states
            normState = np.array([speeds[-1][s] / self.refSpeed[s] for s in G.nodes])

            # Proportional
            proportional = self.kP * errorState

            # Differential
            differential = self.kP * self.Td * self.derivator(errorState) * (errorState > -0.5)

            # Local Control
            localControl = proportional + differential

            # Network data
            _, L, epsilon, _, _ = get_graph_data(G)  # Works because the graph is small

            # Compute neighbor information
            proportionalCO = self.COkP * L @ normState

            # Cooperative term
            neighControl = proportionalCO

            # Memory control
            self.errorSignal.append(errorState)
            self.localU.append(localControl)
            self.coopU.append(neighControl)

            # Total control law
            totalControl = np.clip(
                G.graph["self"] * localControl - (1 - G.graph["self"]) * neighControl, self.uMin, self.uMax
            )

        elif self.typeCtr in ("COPD2", "COST6", "COSTN5"):

            # Compute error
            errorState = np.array([self.refSpeed[s] - speeds[-1][s] for s in G.nodes])

            # Normalized states
            normState = np.array([speeds[-1][s] / self.refSpeed[s] for s in G.nodes])

            # Proportional
            proportional = self.kP * errorState

            # Differential
            differential = self.kP * self.Td * self.derivator(errorState) * (errorState > -0.5)

            # Local Control
            localControl = proportional + differential

            # Network data
            _, L, epsilon, _, _ = get_graph_data(G)  # Works because the graph is small

            # Compute neighbor information
            proportionalCO = self.COkP * L @ normState
            differentialCO = self.COkP * self.COTd * self.derivatorCO(L @ normState)

            # Cooperative term
            neighControl = proportionalCO + differentialCO

            # Memory control
            self.errorSignal.append(errorState)
            self.localU.append(localControl)
            self.coopU.append(neighControl)

            # Total control law
            totalControl = np.clip(
                G.graph["self"] * localControl - (1 - G.graph["self"]) * neighControl, self.uMin, self.uMax
            )
        elif self.typeCtr in ("COPDA", "COSTN6"):
            # Compute error
            errorState = np.array([self.refSpeed[s] - speeds[-1][s] for s in G.nodes])

            # Normalized states
            normState = np.array([speeds[-1][s] / self.refSpeed[s] for s in G.nodes])

            # Proportional
            proportional = self.kP * errorState

            # Differential
            differential = self.kP * self.Td * self.derivator(errorState) * (errorState > -0.5)

            # Local Control
            localControl = proportional + differential

            # Network data
            _, L, epsilon, A, D = get_graph_data(G)  # Works because the graph is small
            d = np.array(list(D.values()))

            meanError = (A + np.eye(*A.shape)) / (d[:, None] + 1) @ errorState
            meanError = np.squeeze(np.asarray(meanError))

            # Compute neighbor information
            proportionalCO = self.COkP * meanError
            differentialCO = self.COkP * self.COTd * self.derivatorCO(meanError)

            # Cooperative term
            neighControl = proportionalCO + differentialCO

            # Memory control
            self.errorSignal.append(errorState)
            self.localU.append(localControl)
            self.coopU.append(neighControl)

            # Total control law
            totalControl = np.clip(
                G.graph["self"] * localControl + (1 - G.graph["self"]) * neighControl, self.uMin, self.uMax
            )
        elif self.typeCtr in ("COPD1MOD", "COSTN7"):
            # Changing scaling factors (Alpha does not exist anymore)

            # Compute error
            errorState = np.array([self.refSpeed[s] - speeds[-1][s] for s in G.nodes])

            # Normalized states
            normState = np.array([speeds[-1][s] / self.refSpeed[s] for s in G.nodes])

            # Proportional
            proportional = self.kP * errorState

            # Differential
            differential = self.kP * self.Td * self.derivator(errorState) * (errorState > -0.5)

            # Local Control
            localControl = proportional + differential

            # Network data
            _, L, epsilon, _, _ = get_graph_data(G)  # Works because the graph is small

            # Compute neighbor information
            proportionalCO = self.COkP * L @ normState

            # Cooperative term
            neighControl = proportionalCO

            # Memory control
            self.errorSignal.append(errorState)
            self.localU.append(localControl)
            self.coopU.append(neighControl)

            # Total control law
            totalControl = np.clip(localControl - neighControl, self.uMin, self.uMax)
        elif self.typeCtr in ("COSTH4",):

            # Compute error
            errorState = np.array([self.refSpeed[s] - speeds[-1][s] for s in G.nodes])

            # Normalized states
            normState = np.array([speeds[-1][s] / self.refSpeed[s] for s in G.nodes])

            # Proportional
            proportional = self.kP * errorState

            # Differential
            differential = self.kP * self.Td * self.derivator(errorState) * (errorState > -0.5)

            # Local Control
            localControl = proportional + differential

            # Network data
            _, L, epsilon, _, _ = get_graph_data(G)  # Works because the graph is small

            # Compute neighbor information
            proportionalCO = self.COkP * L @ normState

            # Cooperative term
            neighControl = proportionalCO

            # Memory control
            self.errorSignal.append(errorState)
            self.localU.append(localControl)
            self.coopU.append(neighControl)

            if simulationstep >= self.trigger:
                # In congestion (Time trigged only local control)
                totalControl = np.clip(localControl, self.uMin, self.uMax)
            else:
                # Total control law
                totalControl = np.clip(
                    G.graph["self"] * localControl - (1 - G.graph["self"]) * neighControl, self.uMin, self.uMax
                )

        elif self.typeCtr in ("COSTH6",):
            # Compute error
            errorState = np.array([self.refSpeed[s] - speeds[-1][s] for s in G.nodes])

            # Normalized states
            normState = np.array([speeds[-1][s] / self.refSpeed[s] for s in G.nodes])

            # Proportional
            proportional = self.kP * errorState

            # Differential
            differential = self.kP * self.Td * self.derivator(errorState) * (errorState > -0.5)

            # Local Control
            localControl = proportional + differential

            # Network data
            _, L, epsilon, A, D = get_graph_data(G)  # Works because the graph is small
            d = np.array(list(D.values()))

            meanError = (A + np.eye(*A.shape)) / (d[:, None] + 1) @ errorState
            meanError = np.squeeze(np.asarray(meanError))

            # Compute neighbor information
            proportionalCO = self.COkP * meanError
            differentialCO = self.COkP * self.COTd * self.derivatorCO(meanError)

            # Cooperative term
            neighControl = proportionalCO + differentialCO

            # Memory control
            self.errorSignal.append(errorState)
            self.localU.append(localControl)
            self.coopU.append(neighControl)

            if simulationstep >= self.trigger:
                # In congestion (Time trigged only local control)
                totalControl = np.clip(localControl, self.uMin, self.uMax)
            else:
                # Total control law
                totalControl = np.clip(
                    G.graph["self"] * localControl + (1 - G.graph["self"]) * neighControl, self.uMin, self.uMax
                )
        else:
            pass

        # Append Control
        self.U.append(totalControl)

        # Formatting control output
        return dict(zip(self.zones, totalControl))

    @property
    def error(self):
        if self.errorSignal:
            return dict(zip(self.zones, self.errorSignal[-1]))
        return dict(zip(self.zones, [] * self.N))

    @property
    def localControl(self):
        if self.localU:
            return dict(zip(self.zones, self.localU[-1]))
        return dict(zip(self.zones, [] * self.N))

    @property
    def cooperativeControl(self):
        if self.localU:
            return dict(zip(self.zones, self.coopU[-1]))
        return dict(zip(self.zones, [] * self.N))

    @property
    def proportionalControl(self):
        if self.typeCtr in ("P", "PI", "PD") and self.proportional is None:
            return dict(zip(self.zones, self.kP * self.errorSignal[-1]))
        return dict(zip(self.zones, [] * self.N))

    @property
    def integralControl(self):
        if self.typeCtr in ("PI",):
            return dict(zip(self.zones, self.integrator.ix[-1]))
        return dict(zip(self.zones, [] * self.N))

    @property
    def derivativeControl(self):
        if self.typeCtr in ("PD",):
            return dict(zip(self.zones, self.derivator.dx[-1]))
        return dict(zip(self.zones, [] * self.N))

    def computeActiveNeighbors(self, G, errorState):

        # Congested neighbors
        activeNeighbors = errorState > 0

        # Pertutation matrix
        permMatrix = block_diag(*activeNeighbors)

        # Data Graph
        _, _, _, A, _ = get_graph_data(G)

        # New adjacency matrix
        APerm = A @ permMatrix

        # New degree
        DPerm = np.sum(APerm, axis=1).reshape(self.N,)

        # Feasibility operation
        # A @ err instead of A @ error / d
        DPerm = np.maximum(DPerm, 1)

        return APerm, DPerm
