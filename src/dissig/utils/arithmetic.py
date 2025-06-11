"""
"""
from __future__ import annotations

import networkx as nx

from dissig.utils.primes import prime_divisors

def macro_lattice(N : int) -> nx.DiGraph:
    assert isinstance(N, int)
    assert N >= 1

    generators = prime_divisors(N)
    
    