#! /usr/bin/env python


# Largest prime factor of the following the following prime number:

import urllib



PRIME_NUMBER = 600851475143
i = 2
biggest_found = 1 # worst case scenario (no factors)


# interesting approach to prime
tmpl = 'http://www.wolframalpha.com/input/?i=is+%d+a+prime+number'
def is_prime(n):
    return ('is a prime number' in urllib.urlopen(tmpl % (n,)).read())


while i * i < PRIME_NUMBER:   # reduce range
    print "Checking " + str(i)
    while PRIME_NUMBER % i == 0:
        PRIME_NUMBER = PRIME_NUMBER / i   # reduce by factor
    i += 1

print PRIME_NUMBER # result after looping
