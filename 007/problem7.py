# !/usr/bin/env python

# Returns a list of primes < n
def primes(n):
    sieve = [True] * n 

    # check up to square root of n because
    # if both a and b > sqrt(n), then a*b > n, so one must be less than or equal to sqrt(n)

    for i in xrange(3, int(n**0.5) + 1, 2):
        if sieve[i]:
            sieve[i*i::2*i] = [False] * ( (n-i*i-1)/(2*i)+1 )

    return [2] + [i for i in xrange(3, n, 2) if sieve[i]]

# starting prime is less than n
# find the x'th prime
def counter(n, x):
    counter = 0 

    initial = primes(n)

    while len(initial) < x:
        n += x # sufficiently large number to step, in this case 10001
        initial = primes(n)

    print initial[x - 1]

counter(10001, 10001)

    



