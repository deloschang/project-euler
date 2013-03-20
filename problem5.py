#!/usr/bin/env python


# Problem 5 Solution
#   2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

#   What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?


def is_evenly_divisible_by(n, x):
    #for j in range(2, x + 1):
        #if not n % j == 0:
            #return False
        
    #return True
    return min(n % j == 0 for j in range(1, x+1))


#def find(x):


#print find(20)
