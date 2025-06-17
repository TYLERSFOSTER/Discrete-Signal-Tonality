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
    tonnetz,
    filename: str,
    appearance_theme='light',
    mode='dot',  # 'dot' uses clusters, no edge classes; 'neato' uses edge classes, no clusters
    prune : bool=False,
):
    assert mode in ['dot', 'neato']
    tone_graph, style = _prepare_graph(tonnetz, appearance_theme, mode, prune)

    if mode == 'dot':
        _apply_dot_layout(tone_graph, tonnetz.sample_count, tonnetz.integer_list, filename, style)
    elif mode == 'neato':
        _apply_neato_layout(tone_graph, tonnetz.sample_count, tonnetz.integer_list, filename, style)


def _prepare_graph(tonnetz, theme, mode, prune):
    G = tonnetz.network.copy()
    modulus = tonnetz.sample_count

    style = _theme_styles(theme)
    for u, v in list(G.edges()):
        w = int(G[u][v]["weight"])
        v_alt = modulus if v == 0 else v

        if (prune or mode=='neato') and (w != 0 and u != 0) and modulus % w == 0 and not (modulus % u == 0 and modulus % v_alt == 0):
            G.remove_edge(u, v)
            continue

        G[u][v]["label"] = str(w)
        G[u][v]["arrowhead"] = "vee"
        G[u][v].update(style="solid", penwidth="1", constraint="true")

        if mode == 'neato':
            if math.gcd(w, modulus) != 1:
                G[u][v].update(color=style["blue"], fontcolor=style["blue"], edge_type="B")
            else:
                G[u][v].update(color=style["red"], fontcolor=style["red"], edge_type="A")
        else:  # dot mode — use neutral styling for all edges
            G[u][v].update(color=style["text"], fontcolor=style["text"])

    for n in G.nodes:
        G.nodes[n].update(
            shape="circle",
            style="filled",
            color=style["text"],
            fillcolor=style["gray"],
            fontcolor=style["text"],
            fontsize="18",
            fixedsize="true",
            width="0.35",
        )

    return G, style


def _apply_dot_layout(G, modulus, integer_list, filename, style):
    aG = to_agraph(G)
    aG.graph_attr.update(
        label=f"\nTonnetz for multipliers {integer_list} in ℤ/{modulus}ℤ\n\n",
        labelloc="t",
        fontsize="24",
        fontcolor=style["text"],
        rankdir="UD",
        compound="true",
        nodesep="0.3",  # ← more horizontal spacing
        ranksep="0.2", # ← more vertical spacing
        bgcolor=style["bg"],
    )

    clusters = unit_clusters(modulus)
    for _, (cluster_name, members) in enumerate(clusters.items()):
        cluster_idx = cluster_name.replace('cluster_','')
        sg = aG.add_subgraph(
            members,
            name=f"cluster_{cluster_idx}",
            label=f"ℤ/{modulus}ℤ-orbit of {cluster_idx}",
            color="red",
            fontsize="16",
            fontcolor="red"
        )

    aG.layout(prog="dot")
    _save_graph_image(aG, filename)


def _apply_neato_layout(G, modulus, integer_list, filename, style):
    aG = to_agraph(G)
    aG.graph_attr.update(
        label=f"\nTonnetz for multipliers {integer_list} in ℤ/{modulus}ℤ\n",
        labelloc="t",
        fontsize="24",
        fontcolor=style["text"],
        bgcolor=style["bg"],
    )
    aG.layout(prog="neato")
    _save_graph_image(aG, filename)


def _save_graph_image(aG, filename):
    project_root = Path(__file__).resolve().parents[3]
    output_dir = project_root / "results" / "tonnetze_visuals"
    output_dir.mkdir(parents=True, exist_ok=True)
    save_path = output_dir / f"{filename}.png"
    aG.draw(save_path)


def _theme_styles(theme):
    return {
        'light': dict(red='red', blue='blue', bg='white', text='black', gray='lightgray'),
        'dark': dict(red='salmon', blue='skyblue', bg='black', text='white', gray='0.35 0.25 0.25'),
    }.get(theme, {
        'red': 'red', 'blue': 'blue', 'bg': 'white', 'text': 'black', 'gray': 'lightgray'
    })
