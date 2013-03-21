#!/usr/env/bin python

# Problem 9 Solution

# a = m^2 - n^2
# b = 2mn
# c = m^2 + n^2


import math

for n in xrange(1, 500): # because the formulas above mean m^2 + mn < 500
    for m in xrange(n + 1, 500):
        a = m**2 - n**2
        b = 2 * m * n
        c = m**2 + n**2

        # only one 
        if a + b + c == 1000:
            answer = a * b * c
            print a, b, c
            print answer
            break


