"""
prime summations
"""

import time

def prime_array(n):
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i ** 2, n + 1, i):
                is_prime[j] = False
    prime = []
    for i in range(len(is_prime)):
        if is_prime[i]:
            prime.append(i)
    return prime

def ways_of_prime(n):
    ways = [0] * (n + 1)
    ways[0] = 1
    coins = prime_array(n)
    for coin in coins:
        for i in range(coin, n + 1):
            ways[i] += ways[i - coin]
    return ways[n]

if __name__ == '__main__':
    start = time.process_time()
    i = 10
    while ways_of_prime(i) <= 5000:
        i += 1
    print(i)
    print('Runtime is ', time.process_time() - start)