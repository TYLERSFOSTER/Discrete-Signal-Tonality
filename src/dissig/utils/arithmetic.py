

def prime_divisors(n):
    factors = []
    d = 2
    while d * d <= n:
        if n % d == 0:
            factors.append(d)
            while n % d == 0:
                n //= d
        d += 1
    if n > 1:
        factors.append(n)
    return factors

# Example usage
number = 120
print(f"Prime divisors of {number}: {prime_divisors(number)}") # Output: Prime divisors of 120: [2, 3, 5]