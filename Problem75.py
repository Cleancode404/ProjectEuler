"""
Singular integer right triangles
"""

import time

def gcd(m, n):
    while n != 0:
        m, n = n, m % n
    return m

def project_euler(limit):
    triangle = [0] * (limit + 1)
    for i in range(2, int((limit // 2) ** 0.5)):
        for j in range(1, i):
            if (i - j) % 2 == 1 and gcd(i, j) == 1:
                s = 2 * i * (i + j)
                for x in range(s, limit + 1, s):
                    triangle[x] += 1
    print(triangle.count(1))

if __name__ == '__main__':
    start = time.process_time()
    project_euler(1500000)
    print('Runtime is ', time.process_time() - start)