"""
Investigating the behaviour of a recursively defined sequence
"""

import math

def cal():
    def f(x):
        return math.floor(2.0** (30.40324278 - x*x)) /1.0e9

    iterations = 10**12

    x, y = -1.0, -1.0
    i = 0
    while i < iterations:
        if i > 0 and x == y:
            break

        x = f(x)
        y = f(f(y))
        i += 1

    remain = (iterations - i) % i
    for i in range(remain):
        x = f(x)
    answer = x + f(x)
    answer = math.floor(answer * 1.0e9) /1.0e9
    return f"{answer:.9f}"


if __name__ == "__main__":
    print(cal)
