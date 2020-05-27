""" 
    Control algorithm
"""

import numpy as np
import networkx as nx
from scipy.sparse import csr_matrix
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

    return P, L, epsilon


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

    def __init__(
        self, G: nx.Graph, samplingTime: float = TS, kP: float = 1, Ti: float = 360, Twd: float = 720, typeCtrl="CO_P"
    ) -> None:
        N = len(G.nodes)
        self.integrator = Integrator(N, samplingTime)
        self.uMax = 1
        self.uMin = 0
        self.kP = kP
        self.Ti = Ti
        self.typeCtr = typeCtrl
        self.Twd = Twd
        self.windReset = np.zeros((1, N))

        # Memory
        self.uKI = []
        self.localU = []
        self.coopU = []
        self.U = []

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

        if self.typeCtr == "P":

            errorState = np.array([G.nodes[s]["freeFlowSpeed"] - speeds[-1][s] for s in G.nodes])
            control = self.kP * errorState
            totalControl = np.clip(control, self.uMin, self.uMax)

        elif self.typeCtr == "PI":

            errorState = np.array([G.nodes[s]["freeFlowSpeed"] - speeds[-1][s] for s in G.nodes])
            proportional = self.kP * errorState
            integral = self.kP * 1 / self.Ti * self.integrator(errorState + self.windReset)
            control = proportional + integral
            boundControl = np.clip(control, self.uMin, self.uMax)

            # Windup (update for next step)
            self.windReset = (boundControl - control) / self.Twd
            totalControl = np.clip(control, self.uMin, self.uMax)

        elif self.typeCtr == "CO_P":
            _, L, epsilon = get_graph_data(G)  # Works because the graph is small
            normState = np.array([speeds[-1][s] / G.nodes[s]["freeFlowSpeed"] for s in G.nodes])

            # Compute local control
            localControl = np.clip(1 - normState, self.uMin, self.uMax)
            self.localU.append(localControl)

            # Compute neighbor information
            proportional = self.kP * epsilon * L @ normState

            # Cooperative term
            neighControl = proportional
            self.coopU.append(neighControl)

            # Total control law
            totalControl = G.graph["self"] * localControl + (1 - G.graph["self"]) * np.clip(
                neighControl, self.uMin, self.uMax
            )

        elif self.typeCtr == "CO_PI":
            _, L, epsilon = get_graph_data(G)  # Works because the graph is small
            normState = np.array([speeds[-1][s] / G.nodes[s]["freeFlowSpeed"] for s in G.nodes])

            # Compute local control
            localControl = np.clip(1 - normState, self.uMin, self.uMax)
            self.localU.append(localControl)

            # Compute neighbor information
            proportional = self.kP * epsilon * L @ normState
            integral = self.kP * 1 / self.Ti * epsilon * L * self.integrator(normState + self.windReset)

            # Cooperative term
            neighControl = proportional + integral
            self.coopU.append(neighControl)
            boundControl = np.clip(neighControl, self.uMin, self.uMax)

            # Windup (update for next step)
            self.windReset = (boundControl - neighControl) / self.Twd

            # Total control law
            totalControl = G.graph["self"] * localControl + (1 - G.graph["self"]) * np.clip(
                neighControl, self.uMin, self.uMax
            )
        # Append Control
        self.U.append(totalControl)

        # Formatting control output
        return dict(zip(speeds[-1].keys(), totalControl))
