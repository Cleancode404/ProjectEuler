#Quadratic primes

import time

def is_prime(n):
    if n == 0 or n == 1:
        return False
    if n % 2 == 2 or n % 3 == 0 or n % 5 == 0 or n % 7 == 0:
        return n == 2 or n == 3 or n == 5 or n == 7
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def quadratic_prime_length(a, b):
    k = 0
    if k ** 2 + k * a + b <= 1:
        return 0
    while k ** 2 + k * a + b > 1 and is_prime(k ** 2 + k * a + b):
        k += 1
    return k

if __name__ == '__main__':
    start = time.time()
    a = 0
    b = 0
    cnt = 0
    for i in range(-999, 1000):
        for j in range(-999, 1000):
            if quadratic_prime_length(i, j ) > cnt:
                cnt = quadratic_prime_length(i, j)
                a = i
                b = j
    print('a = ', a, ', b = ', b, ', a * b = ', a * b, ', cnt = ', cnt)
    print('Runtime is ', time.time() - start)