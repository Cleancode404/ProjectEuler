#largest prime factor
"""
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?
"""""

def prime_factor(n):
    factors = []
    d = 2
    while (d*d <= n):
        while (n>1):
            while n%d == 0:
                factors.append(d)
                n = n/d
            d += 1

    return factors[-1]

print(prime_factor(600851475143))