"""
Test suite for the `primes_below` function.

This script runs unit tests to verify the correctness of the prime number
generation function `primes_below(N)` defined in `primes.py`.
"""
from __future__ import annotations

import pytest

from dissig.utils.primes import primes_below, prime_divisors, prime_powers


@pytest.mark.parametrize("N, primes_list", [
    (2, []),
    (3, [2]),
    (4, [2, 3]),
    (5, [2, 3]),
    (6, [2, 3, 5]),
    (7, [2, 3, 5]),
    (8, [2, 3, 5, 7]),
    (9, [2, 3, 5, 7]),
    (10, [2, 3, 5, 7]),
    (11, [2, 3, 5, 7]),
    (12, [2, 3, 5, 7, 11]),
])
def test_primes_below(N, primes_list):
    """Verify that primes_below returns the expected list"""
    candidate_list = primes_below(N)

    assert isinstance(candidate_list, list)
    assert candidate_list == primes_list


@pytest.mark.parametrize("N, expected", [
        (1, []),
        (2, [2]),
        (3, [3]),
        (4, [2]),
        (6, [2, 3]),
        (8, [2]),
        (9, [3]),
        (12, [2, 3]),
        (17, [17]),
        (18, [2, 3]),
        (60, [2, 3, 5]),
        (97, [97]),
        (100, [2, 5]),
        (121, [11]),
        (2 * 3 * 5 * 7 * 11 * 13, [2, 3, 5, 7, 11, 13]),
])
def test_prime_divisors(N, expected):
    assert prime_divisors(N) == expected


@pytest.mark.parametrize(
    "N, expected",
    [
        (1, []),
        (2, [(2, 1)]),
        (3, [(3, 1)]),
        (4, [(2, 2)]),
        (6, [(2, 1), (3, 1)]),
        (8, [(2, 3)]),
        (9, [(3, 2)]),
        (12, [(2, 2), (3, 1)]),
        (18, [(2, 1), (3, 2)]),
        (60, [(2, 2), (3, 1), (5, 1)]),
        (97, [(97, 1)]),
        (100, [(2, 2), (5, 2)]),
        (121, [(11, 2)]),
        (2 * 3 * 3 * 5 * 5 * 5, [(2, 1), (3, 2), (5, 3)]),
    ]
)
def test_prime_powers(N, expected):
    assert prime_powers(N) == expected