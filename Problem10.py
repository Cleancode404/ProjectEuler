#
# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.
#

"""
Approach
1. identify if a number is prime
2. sum them up below two million
"""
def sum_prime(n):
    sum = 0
    i = 2
    while sum < n:
        if n % i == 0:
            sum = sum + i 
            i += 1
        else:
            i += 1
    return sum

#check solution
print(sum_prime(2000000))

            