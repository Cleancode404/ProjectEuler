"""
order fractions
"""

import time
from pe069 import prime_sieve

def totient(n):
    phi = 1
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            while n % i == 0:
                phi *= i
                n //= i
            phi = phi // i * (i - 1)
    if n > 1:
        phi *= n - 1
    return phi

def totient_array(n):
    array = [x for x in range(n + 1)]
    for i in range(2, n + 1):
        if array[i] == i:
            for j in range(i, n + 1, i):
                array[j] = array[j] // i * (i - 1)
    return array


if __name__ == '__main__':
    start = time.clock_gettime()
    N = 10000000
    prime = prime_sieve(4000)
    answer = 0
    ratio = 3
    for i in range(len(prime)):
        for j in range(i, len(prime)):
            phi = prime[i] * prime[j]
            if phi > N:
                break
            if sorted(str((prime[i] - 1) * (prime[j] - 1))) == sorted(str(phi)) \
                and ratio > phi / ((prime[i] - 1) * (prime[j] - 1)):
                answer = phi
                ratio = phi / ((prime[i] - 1) * (prime[j] - 1))
    print(answer)
    print('Runtime is ', time.clock_gettime() - start)