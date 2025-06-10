"""
Test suite for the `primes_below` function.

This script runs unit tests to verify the correctness of the prime number
generation function `primes_below(N)` defined in `primes.py`.
"""
from __future__ import annotations

import pytest

from dissig.utils.primes import primes_below


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

