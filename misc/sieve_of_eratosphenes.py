# The Sieve of Eratosthenes
def get_primes_before(n):
    prime_candidates = [i for i in range(2, n)]
    next_prime = 2
    prime_index = 1
    multiples = [i for i in range(next_prime * 2, n, next_prime)]
    while next_prime < n and len(multiples) > 0:
        prime_candidates = [i for i in prime_candidates if i not in multiples]
        next_prime = prime_candidates[prime_index]
        prime_index += 1
        multiples = [i for i in range(next_prime * 2, n, next_prime)]
    return prime_candidates

