def prime_factorization(N):
    factors = []
    # Factor out 2s
    while N % 2 == 0:
        factors.append(2)
        N //= 2
    
    # Factor out odd numbers from 3 onwards
    i = 3
    while i * i <= N:
        while N % i == 0:
            factors.append(i)
            N //= i
        i += 2  # only odd numbers
    
    # If N is still > 1, it is a prime
    if N > 1:
        factors.append(N)
    
    return factors


if __name__ == "__main__":
    N = int(input("Enter a number: "))
    print("Prime Factorization:", prime_factorization(N))
