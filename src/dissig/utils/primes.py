"""
dissig.utils.primes: utility for listing all positive integer primes
below a given number
"""
from __future__ import annotations


def primes_below(modulus : int) -> list[int]:
    """
    Returns a list of all prime numbers less than the given integer using
    the Sieve of Eratosthenes algorithm.

    Args:
        modulus: Upper bound (non-inclusive). Finds all primes less than this number

    Returns:
        List of prime numbers less than `modulus`
    """
    if modulus < 2:
        return []

    sieve = [True] * modulus
    sieve[0:2] = [False, False]

    for i in range(2, int(modulus**0.5) + 1):
        if sieve[i]:
            sieve[i*i:modulus:i] = [False] * len(sieve[i*i:modulus:i])

    return [i for i, is_prime in enumerate(sieve) if is_prime]


def prime_divisors(modulus : int) -> list[int]:
    """
    Return the list of distinct prime divisors of a positive integer modulus.

    Parameters:
        modulus (int): A positive integer.

    Returns:
        list[int]: A list of distinct prime numbers that divide modulus.
                   The list is in ascending order.
    """
    assert isinstance(modulus, int)
    assert modulus >= 1

    factors = []
    d = 2
    while d * d <= modulus:
        if modulus % d == 0:
            factors.append(d)
            while modulus % d == 0:
                modulus //= d
        d += 1
    if modulus > 1:
        factors.append(modulus)

    return factors


def prime_powers(modulus : int) -> list:
    """
    Return the list of prime powers in the prime factorization of a positive integer modulus.

    Each element in the result is a tuple (p, e), where p is a prime divisor of modulus,
    and e is the highest exponent such that p**e divides modulus.

    Parameters:
        modulus (int): A positive integer (modulus >= 1).

    Returns:
        list[tuple[int, int]]: A list of (prime, exponent) pairs representing the
        prime power decomposition of modulus, in ascending order of primes.
    """
    assert isinstance(modulus, int)
    assert modulus >= 1

    prime_divisor_list = prime_divisors(modulus)

    ramified_primes = []
    for divisor in prime_divisor_list:
        exponent = 0
        while modulus%divisor**(exponent + 1) == 0:
            exponent += 1

        ramified_primes.append((divisor, exponent))

    return ramified_primes
