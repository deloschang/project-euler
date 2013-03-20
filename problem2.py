# Project Euler Solution for Problem 2


#LIMIT = 10
LIMIT = 4000000

i = 1 # starting number
j = 0 

sum = 0 # sum / answer

while i < LIMIT:
    temp = i
    i = i + j
    j = temp

    if i % 2 == 0 and i <= LIMIT:  # check if even
        sum += i

print sum



