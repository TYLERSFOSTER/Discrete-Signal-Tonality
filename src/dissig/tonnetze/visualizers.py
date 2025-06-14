"""
This script contains functions for visualizing Tonnetz graphs in different styles.
It supports optional clustering based on arithmetic structure (unit classes mod N).
The script dynamically determines the project root and saves output images in
the 'results/tonnetze_visuals' directory.
"""
from __future__ import annotations

from pathlib import Path
import math

from networkx.drawing.nx_agraph import to_agraph

from dissig.tonnetze.networks import Tonnetz
from dissig.utils.arithmetic import unit_clusters


def nx_viz(tonnetz: Tonnetz, filename: str, arithmetic_clusters: bool=True) -> None:
    """
    Renders a Tonnetz graph and saves it as a .png file in the 'results/tonnetze_visuals' directory.

    Optionally groups nodes into subgraphs (clusters) based on their multiplicative equivalence
    classes modulo N, using the `unit_clusters` function.

    Args:
        tonnetz (Tonnetz): A Tonnetz object containing the graph structure, sample count,
                           and integer multipliers.
        filename (str): The name of the file to save the rendered graph as (without file extension).
        arithmetic_clusters (bool): If True, visually group nodes by arithmetic cluster structure
                                    using multiplicative units modulo N. Default is True.

    Returns:
        None: The function writes a PNG file to disk but does not return a value.
    """
    G = tonnetz.network.copy()  # Work on a copy to allow edge removals
    N = tonnetz.sample_count

    # Remove edges that do not map between two divisors of N
    for u, v in list(G.edges()):
        w = int(G[u][v]["weight"])

        if v == 0:
            v_alt = N
        else:
            v_alt = v
        if (w != 0 and u != 0) and N%w == 0 and not (N%u == 0 and N%v_alt == 0):
            G.remove_edge(u, v)
            continue

        G[u][v]["label"] = str(w)
        G[u][v]["arrowhead"] = "vee"

        if math.gcd(w, N) != 1:
            G[u][v]["edge_type"] = "B"
            G[u][v]["color"] = "blue"
            G[u][v]["style"] = "solid"
            G[u][v]["penwidth"] = "2"
            G[u][v]["constraint"] = "true"
        else:
            G[u][v]["edge_type"] = "A"
            G[u][v]["color"] = "red"
            G[u][v]["style"] = "solid"
            G[u][v]["penwidth"] = "2"
            G[u][v]["constraint"] = "true"

    for n in G.nodes:
        G.nodes[n]["shape"] = "circle"
        G.nodes[n]["style"] = "filled"
        G.nodes[n]["fillcolor"] = "lightgray"
        G.nodes[n]["fontsize"] = "24"
        G.nodes[n]["fixedsize"] = "true"
        G.nodes[n]["width"] = "0.5"

    G.graph["label"] = f"\nTonnetz for multipliers {tonnetz.integer_list} in \u2124/{N}\u2124\n "
    G.graph["labelloc"] = "t"
    G.graph["fontsize"] = "38"
    G.graph["rankdir"] = "LR"
    G.graph["compound"] = "true"
    G.graph["nodesep"] = "0.1"
    G.graph["ranksep"] = "2.1"

    A = to_agraph(G)

    if arithmetic_clusters:
        cluster_map = unit_clusters(N)
    else:
        cluster_map = {}
    print("CLUSTER_MAP:", cluster_map)

    for i, (representative, nodes) in enumerate(cluster_map.items()):
        thing = representative.replace('cluster_', '').replace('cluster', '')
        thing = int(thing)

        subgraph_name = f"cluster_{i}"  # must start with "cluster_"
        sub = A.add_subgraph(nodes, name=subgraph_name)
        sub.graph_attr.update(
            label=f"orbit  (\u2124/{N}\u2124)\u002A·{thing%N}",
            style="rounded",
            color="black",
            fontcolor="black",
            fontsize="30em",
            ranksep="1.1",
        )

    A.layout(prog="neato")

    project_root = Path(__file__).resolve().parent.parent.parent.parent
    output_dir = project_root / "results" / "tonnetze_visuals"
    output_dir.mkdir(parents=True, exist_ok=True)

    save_path = output_dir / f"{filename}.png"
    A.draw(save_path)
