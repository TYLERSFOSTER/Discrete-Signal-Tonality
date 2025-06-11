"""
Test suite for the `primes_below` function.

This script runs unit tests to verify the correctness of the prime number
generation function `primes_below(N)` defined in `primes.py`.
"""
from __future__ import annotations

import numpy as np
import pytest
import networkx as nx
import matplotlib.pyplot as plt
from networkx.drawing.nx_agraph import to_agraph

from dissig.tonnetze.network import Tonnetz
from dissig.utils.primes import primes_below


@pytest.mark.parametrize("N, integer_list", [
    (12, [2, 3, 5, 7]),
])
def test_primes_below(N, integer_list):
    """Verify that primes_below returns the expected list"""
    resulting_tonnetz = Tonnetz(N, integer_list, include_loops=True, include_zero=True)
    print("Network nodes:", resulting_tonnetz.network.nodes)
    print("Network edges:", resulting_tonnetz.network.edges)

    G = resulting_tonnetz.network
    
    # pos = nx.spectral_layout(G)
    # perturbation_scale = 0.15
    # for node in pos:
    #     pos[node] += np.random.normal(scale=perturbation_scale, size=2)
    # nx.draw_networkx_nodes(G, pos, node_color='lightblue', node_size=400)
    # nx.draw_networkx_labels(G, pos, font_size=12)
    # nx.draw_networkx_edges(G, pos, arrows=True, arrowstyle='->',
    #                     connectionstyle='arc3,rad=0.05')
    # edge_labels = nx.get_edge_attributes(G, 'weight')
    # nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=6)
    # plt.axis('off')
    # plt.show()

    for u, v, d in G.edges(data=True):
        d["label"] = str(d["weight"])
        d["arrowhead"] = "vee"  # "normal", "vee", "diamond", etc.
    for n in G.nodes:
        G.nodes[n]["shape"] = "circle"
        G.nodes[n]["style"] = "filled"
        G.nodes[n]["fillcolor"] = "lightgray"  # or a hex code like "#dddddd"
        G.nodes[n]["fontsize"] = "24"        # font size in points
        G.nodes[n]["fixedsize"] = "true"     # prevent resizing to label
        G.nodes[n]["width"] = "0.5"          # diameter in inches
    G.graph["label"] = f"\nTonnetz for multipliers {resulting_tonnetz.integer_list} in \u2124/{N}\u2124\n "
    G.graph["labelloc"] = "t"
    G.graph["fontsize"] = "18"
    G.graph["rankdir"] = "LR"
    A = to_agraph(G)
    print("NODES:", A.nodes())
    cluster_map = {
        "cluster_1": ['1', '5', '7', '11'],
        "cluster_2": ['2', '10'],
        "cluster_4": ['4', '8'],
        "cluster_3": ['3', '9'],
        "cluster_6": ['6'],
        "cluster_12": ['0'],
    }
    for i, (name, nodes) in enumerate(cluster_map.items()):
        sub = A.add_subgraph(nodes, name=name)
        sub.graph_attr.update(
            label=name, 
            style="rounded", 
            color="red",
            ranksep="1",
        )
    A.layout("dot")
    A.draw("graph.png")

    assert False

if __name__ == "__main__":
    N = 10
    test_primes_below(N, primes_below(N))