#
# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.
#

"""
Approach
1. identify if a number is prime
2. sum them up below two million
"""
import math
def sum_prime(num):
    for i in range(2, int(math.sqrt(num))+1 ):
        if (num % i == 0):
            return False
    return True

sum = 0

for i in range(2, 2000000):
    if sum_prime(i):
        sum += i

print(sum)


            