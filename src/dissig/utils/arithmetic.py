"""
./src/dissig/utils/arithmetic.py
"""
from __future__ import annotations

import math


def all_divisors(modulus : int) -> list[int]:
    """
    Compute all positive divisors of a given positive integer modulus.

    Args:
        modulus (int): A positive integer.

    Returns:
        list[int]: A sorted list of all positive divisors of modulus.
    """
    assert isinstance(modulus, int)
    assert modulus > 0, "Input must be a positive integer"

    result = set()

    for i in range(1, int(modulus**0.5) + 1):
        if modulus % i == 0:
            result.add(i)
            result.add(modulus // i)

    sorted_list = sorted(result)

    return sorted_list


def multiplicative_units(modulus : int) -> list[int]:
    """
    Compute the multiplicative units in the ring Z/modulusZ.

    Args:
        modulus (int): A positive integer.

    Returns:
        list[int]: A list of integers in {0, ..., modulus-1} that are coprime to modulus.
    """
    assert isinstance(modulus, int)

    unit_list = [idx for idx in range(modulus) if math.gcd(idx, modulus) == 1]

    return unit_list


def unit_clusters(modulus : int) -> dict[str, list[int]]:
    """
    Compute clusters in Z/modulusZ formed by multiplying base cluster, consisting of
    units (Z/modulusZ)^× in Z/modulusZ by every divisor of modulus.

    Args:
        modulus (int): A positive integer.

    Returns:
        dict[str, list[int]]: A dictionary mapping 'cluster_d' to the sorted list
            of residues {(d * u) mod modulus | u in (Z/modulusZ)^×}, for each divisor d of modulus.
    """
    assert isinstance(modulus, int)
    assert modulus >= 1

    ring_units = multiplicative_units(modulus)

    clusters = {}
    for divisor in all_divisors(modulus):
        new_cluster = [(divisor * idx)%modulus for idx in ring_units]
        new_cluster = list(set(new_cluster))
        new_cluster = sorted(new_cluster)

        cluster_label = f"cluster_{divisor}"
        clusters[cluster_label] = new_cluster

    return clusters


def unit_vectors(modulus: int) -> list[tuple[float, float]]:
    """
    Returns modulus unit vectors (as 2D tuples) corresponding to angles
    from π/2 to π/2 - (modulus - 1)·π/modulus, stepping by -π/modulus.

    Args:
        modulus (int): Number of unit vectors to generate.

    Returns:
        List[Tuple[float, float]]: List of 2D unit vectors (cos(θ), sin(θ)).
    """
    assert isinstance(modulus, int) and modulus >= 1

    vectors = [
        (math.cos(math.pi/2 - k * math.pi/modulus), math.sin(math.pi/2 - k * math.pi/modulus))
        for k in range(modulus)
    ]

    return vectors
