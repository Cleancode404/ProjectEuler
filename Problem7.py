#10001th prime number
"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, 
we can see that the 6th prime is 13.
What is the 10 001st prime number?
"""

#check if a number is prime
def isPrime(n):
    if n < 2:
        return "Not a prime"
    for i in range(2, int(n**.5) + 1 ):
        if n % i == 0:
            return False
    return True

#find out the nth prime
def nthPrime(n):
    term = 0
    prime = 1
    while term < n:
        prime = prime + 1
        if isPrime(prime):
            term = term + 1
    return prime

print(nthPrime(10001))
