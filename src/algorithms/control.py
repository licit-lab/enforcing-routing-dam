""" 
    Control algorithm
"""

import numpy as np
import networkx as nx
from scipy.sparse import csr_matrix

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

# ======================================================================================================================
# Functions
# ======================================================================================================================


# Cooperative graph
def define_grid_graph(N: int = 3, M: int = 3, mapping: dict = DEFAULT_MAP) -> nx.Graph:
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
    P = np.identity(N * N) - epsilon * L

    return P, L, epsilon


def compute_vanishing_control(speeds: dict, G: nx.Graph) -> dict:
    """ Computes the control law based on current speeds and some graph information

    :param speeds: dictionary of speed per zone
    :type speeds: dict
    :param G: undirected graph for cooperativity 
    :type G: nx.Graph
    :return: vanishing policy per zone 
    :rtype: dict
    """

    # Network layout creation
    _, L, epsilon = get_graph_data(G)  # Works because the graph is small
    control = epsilon * L.toarray() @ np.array(list(speeds.values()))  # Consensus protocol
    return dict(zip(speeds.keys(), control))
