"""
"""
from __future__ import annotations

import math

import numpy as np

from dissig.utils.primes import prime_divisors


def unit_vectors(N: int) -> list[tuple[float, float]]:
    """
    Returns N unit vectors (as 2D tuples) corresponding to angles
    from π/2 to π/2 - (N - 1)·π/N, stepping by -π/N.

    Args:
        N (int): Number of unit vectors to generate.

    Returns:
        List[Tuple[float, float]]: List of 2D unit vectors (cos(θ), sin(θ)).
    """
    assert isinstance(N, int) and N >= 1

    vectors = [
        (math.cos(math.pi/2 - k * math.pi/N), math.sin(math.pi/2 - k * math.pi/N))
        for k in range(N)
    ]

    return vectors


def macro_lattice(N : int) -> list[tuple[float, float]]:
    assert isinstance(N, int)
    assert N >= 1

    prime_divisor_list = prime_divisors(N)

    lattice_rank = len(prime_divisor_list)

    lattice_generator_pairs = unit_vectors(lattice_rank)
    lattice_generator_vectors = [np.array(divisor) for divisor in lattice_generator_pairs]

    pass
    