#! /usr/bin/env python

# Project Euler Solution for Problem 2


#LIMIT = 10
LIMIT = 4000000

i,j = 1, 0 # starting vars

sum = 0 # sum / answer

while i <= LIMIT:
    temp = i
    i,j = i + j, temp

    if i % 2 == 0 and i <= LIMIT:  # check if even, test limit again
        sum += i

print sum # print answer



