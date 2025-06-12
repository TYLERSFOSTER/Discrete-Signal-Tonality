"""
This script contains functions for visualizing Tonnetz graphs in different styles.
It supports optional clustering based on arithmetic structure (unit classes mod N).
The script dynamically determines the project root and saves output images in
the 'results/tonnetze_visuals' directory.
"""
from __future__ import annotations

from pathlib import Path
from networkx.drawing.nx_agraph import to_agraph

from dissig.tonnetze.network import Tonnetz
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
    G = tonnetz.network
    N = tonnetz.sample_count

    for _, _, d in G.edges(data=True):
        d["label"] = str(d["weight"])
        d["arrowhead"] = "vee"

    for n in G.nodes:
        G.nodes[n]["shape"] = "circle"
        G.nodes[n]["style"] = "filled"
        G.nodes[n]["fillcolor"] = "lightgray"
        G.nodes[n]["fontsize"] = "24"
        G.nodes[n]["fixedsize"] = "true"
        G.nodes[n]["width"] = "0.5"

    G.graph["label"] = f"\nTonnetz for multipliers {tonnetz.integer_list} in \u2124/{N}\u2124\n "
    G.graph["labelloc"] = "t"
    G.graph["fontsize"] = "18"
    G.graph["rankdir"] = "LR"

    A = to_agraph(G)

    if arithmetic_clusters:
        cluster_map = unit_clusters(N)
    else:
        cluster_map = {}
    print("CLUSTER_MAP:", cluster_map)

    for _, (name, nodes) in enumerate(cluster_map.items()):
        sub = A.add_subgraph(nodes, name=name)
        sub.graph_attr.update(
            label=name,
            style="rounded",
            color="red",
            ranksep="1",
        )

    A.layout("dot")
    A.draw("graph.png")

    project_root = Path(__file__).resolve().parents[1]
    output_dir = project_root / "results" / "tonnetze_visuals"
    output_dir.mkdir(parents=True, exist_ok=True)

    save_path = output_dir / f"{filename}.png"
    A.draw(save_path)
