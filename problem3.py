# Largest prime factor of the following:

import urllib



PRIME_NUMBER = 600851475143
biggest_found = 1 # worst case scenario

# takes in number and tells you if prime or not
tmpl = 'http://www.wolframalpha.com/input/?i=is+%d+a+prime+number'
def is_prime(n):
    return ('is a prime number' in urllib.urlopen(tmpl % (n,)).read())


is_prime(2)
#for i in reversed(range(3, PRIME_NUMBER)): # loop through the primes
    #if PRIME_NUMBER % i == 0 and prime(i):  # is a factor
        #biggest_found = i  # save largest found
        #print biggest_found

#print biggest_found # result after looping
