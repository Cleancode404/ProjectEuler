"""
Red, green or blue tiles
"""

def f(m, n):
    ways = [0] * (n + 1)
    for i in range(m):
        ways[i] = 1
    for i in range(m, n + 1):
        ways[i] += ways[i - 1] + ways[i - m]
    return ways[n] - 1

if __name__ == '__main__':
    print(f(2, 50) + f(3, 50) + f(4, 50))