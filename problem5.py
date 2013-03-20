#!/usr/bin/env python


# Problem 5 Solution
#   2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

#   What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?


def factorize(x):
    # < 11 don't need to be checked because 12-20 implicitly checks them
    i = 380 # because 19*2, 19*3 ... 19*19 not divis by 20
            # so increment by 380 as well
    solved = False

    while not solved:
        solved = i % 11 == 0 and i % 12 == 0 and i % 13 == 0 and \
                i % 14 == 0 and i % 15 == 0 and i % 16 == 0 and \
                i % 17 == 0 and i % 18 == 0 and i % 19 == 0 and \
                i % 20 == 0

        if not solved:
            i += 380

    return i


print factorize(20)
