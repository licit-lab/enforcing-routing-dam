""" 
    Control algorithm
"""

import numpy as np
import networkx as nx
from scipy.sparse import csr_matrix
from itertools import repeat
from .pid import PIDantiwindup

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

# ======================================================================================================================
# Functions
# ======================================================================================================================


# Cooperative graph
def define_grid_graph(N: int = 3, M: int = 3, mapping: dict = DEFAULT_MAP, refSpeed: dict = DEFAULT_SPD) -> nx.Graph:
    """ Creates a grid graph for the control algorithm 
    
    :param N: row number, defaults to 3
    :type N: int, optional
    :param M: column number, defaults to 3
    :type M: int, optional
    :param mapping: mapping option to match symuvia, defaults to DEFAULT_MAP
    :type mapping: dict, optional
    :return: tuple with 
    :rtype: tuple
    """

    # Creating cyclic  graph
    G = nx.grid_2d_graph(N, M)

    # Relabeling nodes
    # mapping = dict(zip(F.nodes(),sensors))

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


def compute_vanishing_control(simulationstep: int, triggertime: int, speeds: list, G: nx.Graph) -> dict:
    """ Computes the control law based on current speeds and some graph information

    :param speeds: list of cumulated speeds
    :type speeds: dict
    :param G: undirected graph for cooperativity 
    :type G: nx.Graph
    :return: vanishing policy per zone 
    :rtype: dict
    """

    # Case speed is empty
    if not speeds:
        return dict(zip(list(G.nodes), repeat(0)))

    # Network layout creation
    P, L, epsilon = get_graph_data(G)  # Works because the graph is small

    # Compute normalized states
    normState = np.array([speeds[-1][s] / G.nodes[s]["freeFlowSpeed"] for s in G.nodes])

    # Compute local control
    localControl = 0.5 * np.maximum(1 - normState, 0)

    # Compute neighbor information
    neighControl = 0.5 * epsilon * L @ normState

    totalControl = localControl + np.maximum(neighControl, 0)

    return dict(zip(speeds[-1].keys(), totalControl))


def compute_pid_vanishing_control(simulationstep: int, triggertime: int, speeds: list, G: nx.Graph) -> dict:
    """    
    :param speeds: [description]
    :type speeds: dict
    :param G: [description]
    :type G: nx.Graph
    :return: [description]
    :rtype: dicts
    """

    # PID

    u = PIDantiwindup(k_p=0.1, k_d=0.1, k_i=0.1)
