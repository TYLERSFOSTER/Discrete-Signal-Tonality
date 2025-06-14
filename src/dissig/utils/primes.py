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


def prime_divisors(N : int) -> list[int]:
    """
    Return the list of distinct prime divisors of a positive integer N.

    Parameters:
        N (int): A positive integer.

    Returns:
        list[int]: A list of distinct prime numbers that divide N.
                   The list is in ascending order.
    """
    assert isinstance(N, int)
    assert N >= 1

    factors = []
    d = 2
    while d * d <= N:
        if N % d == 0:
            factors.append(d)
            while N % d == 0:
                N //= d
        d += 1
    if N > 1:
        factors.append(N)

    return factors


def prime_powers(N : int) -> list:
    """
    Return the list of prime powers in the prime factorization of a positive integer N.

    Each element in the result is a tuple (p, e), where p is a prime divisor of N,
    and e is the highest exponent such that p**e divides N.

    Parameters:
        N (int): A positive integer (N >= 1).

    Returns:
        list[tuple[int, int]]: A list of (prime, exponent) pairs representing the
        prime power decomposition of N, in ascending order of primes.
    """
    assert isinstance(N, int)
    assert N >= 1

    prime_divisor_list = prime_divisors(N)

    ramified_primes = []
    for divisor in prime_divisor_list:
        exponent = 0
        while N%divisor**(exponent + 1) == 0:
            exponent += 1

        ramified_primes.append((divisor, exponent))

    return ramified_primes
