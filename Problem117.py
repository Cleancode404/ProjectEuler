"""
Red, green or blue tiles
"""

def f(n):
    ways = [0] * (n + 1)
    ways[0] = 1
    for i in range(1, n + 1):
        ways[i] += ways[i -1]
        if i >= 2:
            ways[i] += ways[i - 2]
        if i >= 3:
            ways[i] += ways[i - 3]
        if i >= 4:
            ways[i] += ways[i - 4]
    return ways[n]

if __name__ == '__main__':
    print(f(50))