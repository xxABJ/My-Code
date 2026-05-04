def sieve(n):
    """Return a list of primes up to n using the Sieve of Eratosthenes."""
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False

    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]:
            for j in range(i*i, n + 1, i):
                is_prime[j] = False

    return is_prime


def goldbach_count(N):
    """Return the number of Goldbach pairs for even N."""
    primes = sieve(N)
    count = 0

    for p in range(2, N // 2 + 1):
        q = N - p
        if primes[p] and primes[q]:
            count += 1

    return count


# Example: count Goldbach pairs for 10,000
print(goldbach_count(1000000))