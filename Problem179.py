"""
Consecutive positive divisors
"""

import time

if __name__ == '__main__':
    start = time.process_time()
    divisor = [2]*10000001
    divisor[0], divisor[1] = 0, 1
    for i in range(2, int(10000001**0.5) + 1):
        divisor[i * i] -= 1
        for j in range(i * i, 10000001 , i):
            divisor[j] += 2
    print(sum(1 if divisor[i] == divisor[i + 1] else 0 for i in range(2, 10000000)))
    print('Runtime is', time.process_time() - start)