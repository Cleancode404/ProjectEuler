"""
Odd period square roots 
"""""

import time

def get_square_root(n):
    root = []
    period = []
    cache = []
    x, y = 0, 1
    while (x + 1) ** 2 <= n:
        x += 1
    root.append(x)
    if x ** 2 != n:
        while (x, y) not in cache:
            cache.append((x, y))
            k = 0
            d = (n - x ** 2) // y
            while ((k + 1) * d - x) ** 2 <= n:
                k += 1
            period.append(k)
            x, y = k * d - x, d
    root.append(period)
    return root

if __name__ == '__main__':
    start = time.process_time()
    N = 10000
    count = 0
    for i in range(N + 1):
        if len(get_square_root(i)[-1]) % 2 == 1:
            count += 1
    print(count)
    print('Runtime is ', time.process_time() - start)
