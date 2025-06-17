"""
Script for generating images of tonnetze
"""
from __future__ import annotations

import networkx as nx
import matplotlib.pyplot as plt

from dissig.tonnetze.networks import Tonnetz
from dissig.tonnetze.visualizers import nx_viz

if __name__ == "__main__":
    modulus = 36
    integer_list = [2, 3, 5, 7]

    tonnetz = Tonnetz(modulus, integer_list)

    nx_viz(tonnetz, "test_viz", mode='neato', appearance_theme='dark')

    # Create a graph
    G = tonnetz.network
    print('tonnetz.network:', G)
    print("tonnetz.network.nodes:", G.nodes)
    print("tonnetz.network.edges:", len(G.edges))
    
    nx.draw(G, with_labels=True)
    
    plt.show()