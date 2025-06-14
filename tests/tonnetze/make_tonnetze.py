"""
"""
from __future__ import annotations

from dissig.tonnetze.networks import Tonnetz
from dissig.tonnetze.visualizers import nx_viz

if __name__ == "__main__":
    tonnetz = Tonnetz(8*9*3, [2, 3, 5, 11, 13])
    nx_viz(tonnetz, "test_viz", appearance_theme='dark')