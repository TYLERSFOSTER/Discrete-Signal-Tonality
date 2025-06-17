"""
Script for generating images of tonnetze
"""
from __future__ import annotations

from dissig.tonnetze.networks import Tonnetz
from dissig.tonnetze.visualizers import nx_viz

if __name__ == "__main__":
    modulus = 35
    integer_list = [2, 3, 5, 7]

    tonnetz = Tonnetz(modulus, integer_list)

    nx_viz(tonnetz, "test_viz", mode='neato', appearance_theme='dark')