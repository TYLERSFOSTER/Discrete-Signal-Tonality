"""
This script contains functions for visualizing Tonnetz graphs in different styles.
It supports optional clustering based on arithmetic structure (unit classes mod modulus).
The script dynamically determines the project root and saves output images in
the 'results/tonnetze_visuals' directory.
"""
from __future__ import annotations

from pathlib import Path
import math

from networkx.drawing.nx_agraph import to_agraph

from dissig.tonnetze.networks import Tonnetz
from dissig.utils.arithmetic import unit_clusters


def nx_viz(
    tonnetz: Tonnetz,
    filename: str,
    arithmetic_clusters: bool=True,
    appearance_theme='light',
) -> None:
    """
    Renders a Tonnetz graph and saves it as a .png file in the 'results/tonnetze_visuals' directory.

    Optionally groups nodes into subgraphs (clusters) based on their multiplicative equivalence
    classes modulo modulus, using the `unit_clusters` function.

    Args:
        tonnetz (Tonnetz): A Tonnetz object containing the graph structure, sample count,
                           and integer multipliers.
        filename (str): The name of the file to save the rendered graph as (without file extension).
        arithmetic_clusters (bool): If True, visually group nodes by arithmetic cluster structure
                                    using multiplicative units modulo modulus. Default is True.

    Returns:
        None: The function writes a PNG file to disk but does not return a value.
    """
    assert appearance_theme in ['light', 'dark']
    if appearance_theme == 'light':
        red_hue = 'red'
        blue_hue = 'blue'
        background_hue = 'white'
        text_hue = 'black'
        gray_hue = 'lightgray'
    elif appearance_theme == 'dark':
        red_hue = 'salmon'
        blue_hue = 'skyblue'
        background_hue = 'black'
        text_hue = 'white'
        gray_hue = '0.35 0.25 0.25'
    else:
        red_hue = 'red'
        blue_hue = 'blue'
        background_hue = 'white'
        text_hue = 'black'
        gray_hue = 'lightgray'

    tone_graph = tonnetz.network.copy()  # Work on a copy to allow edge removals
    modulus = tonnetz.sample_count

    # Remove edges that do not map between two divisors of modulus
    for u, v in list(tone_graph.edges()):
        w = int(tone_graph[u][v]["weight"])

        if v == 0:
            v_alt = modulus
        else:
            v_alt = v
        if (w != 0 and u != 0) and modulus%w == 0 and not (modulus%u == 0 and modulus%v_alt == 0):
            tone_graph.remove_edge(u, v)
            continue

        tone_graph[u][v]["label"] = str(w)
        tone_graph[u][v]["arrowhead"] = "vee"

        if math.gcd(w, modulus) != 1:
            tone_graph[u][v]["edge_type"] = "B"
            tone_graph[u][v]["color"] = blue_hue
            tone_graph[u][v]["style"] = "solid"
            tone_graph[u][v]["penwidth"] = "1"
            tone_graph[u][v]["fontcolor"] = blue_hue
            tone_graph[u][v]["constraint"] = "true"
        else:
            tone_graph[u][v]["edge_type"] = "A"
            tone_graph[u][v]["color"] = red_hue
            tone_graph[u][v]["style"] = "solid"
            tone_graph[u][v]["penwidth"] = "1"
            tone_graph[u][v]["fontcolor"] = red_hue
            tone_graph[u][v]["constraint"] = "true"

    for n in tone_graph.nodes:
        tone_graph.nodes[n]["shape"] = "circle"
        tone_graph.nodes[n]["style"] = "filled"
        tone_graph.nodes[n]["color"] = text_hue
        tone_graph.nodes[n]["fillcolor"] = gray_hue
        tone_graph.nodes[n]["fontcolor"] = text_hue
        tone_graph.nodes[n]["fontsize"] = "18"
        tone_graph.nodes[n]["fixedsize"] = "true"
        tone_graph.nodes[n]["width"] = "0.35"

    tone_graph.graph["label"] = (
        f"\nTonnetz for multipliers {tonnetz.integer_list} "
        f"in \u2124/{modulus}\u2124\n"
    )
    tone_graph.graph["labelloc"] = "t"
    tone_graph.graph["fontsize"] = "24"
    tone_graph.graph["fontcolor"] = text_hue
    tone_graph.graph["rankdir"] = "LR"
    tone_graph.graph["compound"] = "true"
    tone_graph.graph["nodesep"] = "0.1"
    tone_graph.graph["ranksep"] = "2.1"
    tone_graph.graph["bgcolor"] = background_hue  # <--- This line sets the full image background

    a_graph = to_agraph(tone_graph)

    if arithmetic_clusters:
        cluster_map = unit_clusters(modulus)
    else:
        cluster_map = {}
    print("CLUSTER_MAP:", cluster_map)

    for _, (representative, _) in enumerate(cluster_map.items()):
        thing = representative.replace('cluster_', '').replace('cluster', '')
        thing = int(thing)

    a_graph.layout(prog="neato")

    project_root = Path(__file__).resolve().parent.parent.parent.parent
    output_dir = project_root / "results" / "tonnetze_visuals"
    output_dir.mkdir(parents=True, exist_ok=True)

    save_path = output_dir / f"{filename}.png"
    a_graph.draw(save_path)
