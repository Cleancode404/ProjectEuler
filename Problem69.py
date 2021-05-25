"""
totient maximum
"""

import time

__date__ = '14-4-4'
__author__ = 'SUN'

def prime_sieve(limit):
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(limit ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i ** 2, limit + 1, i):
                is_prime[j] = False
    prime = []
    for i in range(limit + 1):
        if is_prime[i]:
            prime.append(i)
    return prime

if __name__ == '__main__':
    start = time.clock()
    N = 1000000
    prime = prime_sieve(30)
    answer = 1
    for x in prime:
        if answer * x > N:
            break
        answer *= x
    print(answer)
    print('Runtime is ', time.clock() - start)