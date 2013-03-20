# Problem 6 Solution

n = 100

def square_of_sum(i):
    return (i * (i+1) / 2)**2

def sum_of_squares(i):
    return i * (i + 1) * (2 * i + 1) / 6


def difference(a, b):
    print a - b

difference(square_of_sum(n) , sum_of_squares(n))
