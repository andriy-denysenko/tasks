def nth_prime(n):
    # Start from the first integer
    prime_candidate = 1
    # Count to n-th prime
    i = 0
    while i < n:
        # Increment the candidate it at the beginning of the loop to stop on the n-th candidate
        prime_candidate += 1
        if is_prime(prime_candidate):
            i += 1
    return prime_candidate
        
        
        
def is_prime(prime_candidate):
    # Try to divide by 2..previous number
    divisor = 2
    while divisor < prime_candidate and prime_candidate % divisor != 0:
        divisor += 1
    # If the last divisor is the number itself, the prime_candidate is a prime number
    return True if divisor == prime_candidate else False
        