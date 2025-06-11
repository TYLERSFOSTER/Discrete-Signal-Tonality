"""
This script contains functions for visualizing Tonnetz graphs in different styles.
The script dynamically determines the project root and saves the output images in
the 'results/tonnetze_visuals' directory.
"""
from __future__ import annotations

from pathlib import Path

from networkx.drawing.nx_agraph import to_agraph

from dissig.tonnetze.network import Tonnetz


def nx_viz(tonnetz: Tonnetz, filename: str) -> None:
    """
    Renders a Tonnetz graph and saves it as a .png file in the 'results/tonnetze_visuals' directory.

    Args:
        tonnetz (Tonnetz): A Tonnetz object containing the graph structure and sample count.
        filename (str): The name of the file to save the rendered graph as (without file extension).

    Returns:
        None: This function does not return any value. It saves the rendered graph as a .png file.
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

    G.graph["label"] = f"\nTonnetz for multipliers {tonnetz.integer_list} in ℤ/{N}ℤ\n"
    G.graph["labelloc"] = "t"
    G.graph["fontsize"] = "18"
    G.graph["rankdir"] = "UD"
    
    project_root = Path(__file__).resolve().parents[1]
    output_dir = project_root / "results" / "tonnetze_visuals"
    output_dir.mkdir(parents=True, exist_ok=True)

    save_path = output_dir / f"{filename}.png"

    A = to_agraph(G)
    A.layout("dot")


def arithmetic_viz(tonnetz: Tonnetz, filename: str) -> None:
    """
    Placeholder function for rendering an arithmetic-based visualization of the Tonnetz graph.

    Args:
        tonnetz (Tonnetz): A Tonnetz object containing the graph structure.
        filename (str): The name of the file to save the arithmetic-based graph as (without file extension).

    Returns:
        None: This function does not return any value. It will save the arithmetic-based graph once implemented.
    """
    pass