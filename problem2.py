# Project Euler Solution for Problem 2


LIMIT = 10
#LIMIT = 4000000;

i = 1 # starting number
j = 0 

for q in range(LIMIT + 1):
    temp = i
    i = i + j
    j = temp
    print i



