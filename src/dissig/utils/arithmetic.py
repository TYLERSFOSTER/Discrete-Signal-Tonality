"""
./src/dissig/utils/arithmetic.py
"""
from __future__ import annotations

import math


def all_divisors(N : int) -> list[int]:
    """
    Compute all positive divisors of a given positive integer N.

    Args:
        N (int): A positive integer.

    Returns:
        list[int]: A sorted list of all positive divisors of N.
    """
    assert isinstance(N, int)
    assert N > 0, "Input must be a positive integer"

    result = set()

    for i in range(1, int(N**0.5) + 1):
        if N % i == 0:
            result.add(i)
            result.add(N // i)

    sorted_list = sorted(result)

    return sorted_list


def multiplicative_units(N : int) -> list[int]:
    """
    Compute the multiplicative units in the ring Z/NZ.

    Args:
        N (int): A positive integer.

    Returns:
        list[int]: A list of integers in {0, ..., N-1} that are coprime to N.
    """
    assert isinstance(N, int)

    unit_list = [idx for idx in range(N) if math.gcd(idx, N) == 1]

    return unit_list


def unit_clusters(N : int) -> dict[str, list[int]]:
    """
    Compute clusters in Z/NZ formed by multiplying base cluster, consisting of
    units (Z/NZ)^× in Z/NZ by every divisor of N.

    Args:
        N (int): A positive integer.

    Returns:
        dict[str, list[int]]: A dictionary mapping 'cluster_d' to the sorted list
                              of residues {(d * u) mod N | u in (Z/NZ)^×}, for each divisor d of N.
    """
    assert isinstance(N, int)
    assert N >= 1

    ring_units = multiplicative_units(N)

    clusters = {}
    for divisor in all_divisors(N):
        new_cluster = [(divisor * idx)%N for idx in ring_units]
        new_cluster = list(set(new_cluster))
        new_cluster = sorted(new_cluster)

        cluster_label = f"cluster_{divisor}"
        clusters[cluster_label] = new_cluster

    return clusters


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
