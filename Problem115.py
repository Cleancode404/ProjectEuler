"""
Counting block combinations II

"""

def f(m, n):
    ways = [0] * (n + 1)
    for i in range(m):
        ways[i] = 1
        
    for i in range(m, n + 1):
        ways[i] += ways[i - 1] + 1
        for j in range(m, i):
            ways[i] += ways[i - j -1]
    return ways[n]


if __name__ == "__main__":
    i = 50
    while f(50, i) <= 1000000:
        i += 1
    print(i)