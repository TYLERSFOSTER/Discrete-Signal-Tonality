"""
dissig.utils.primes: utility for listing all positive integer primes
below a given number
"""
from __future__ import annotations


def primes_below(N : int) -> list[int]:
    """
    Returns a list of all prime numbers less than the given integer using
    the Sieve of Eratosthenes algorithm.

    Args:
        N: Upper bound (non-inclusive). Finds all primes less than this number

    Returns:
        List of prime numbers less than `N`
    """
    if N < 2:
        return []

    sieve = [True] * N
    sieve[0:2] = [False, False]

    for i in range(2, int(N**0.5) + 1):
        if sieve[i]:
            sieve[i*i:N:i] = [False] * len(sieve[i*i:N:i])

    return [i for i, is_prime in enumerate(sieve) if is_prime]

