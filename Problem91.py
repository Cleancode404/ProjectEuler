"""
Right triangles with integer coordinates
"""

import time


if __name__ == '__main__':
    start = time.clock()
    N = 50
    answer = N * N
    for x1 in range(N + 1):
        for y1 in range(N + 1):
            for x2 in range(N + 1):
                for y2 in range(N + 1):
                    if x1 == 0 and y1 == 0 or x2 == 0 and y2 == 0:
                        continue
                    if x1 ** 2 + y1 ** 2 - x1 * x2 - y1 * y2 == 0 and (x1 != x2 or y1 != y2):
                        answer += 1
    print(answer)
    print('Runtime is', time.clock() - start)