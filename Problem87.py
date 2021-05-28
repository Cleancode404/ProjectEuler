"""
Prime power triples
"""


def prime(n):
    array = [True] * n
    array[0] = array[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if array[i]:
            for j in range(2 * i, n, i):
                array[j] = False
    p = []
    for i in range(n):
        if array[i]:
            p.append(i)
    return p

if __name__ == '__main__':
    N = 50000000
    i = 1
    while i ** 2 + i ** 3 + i ** 4 < N:
        i += 1
    i -= 1

    m2 = m3 = m4 = 0
    a = prime(10000)
    for i in range(len(a)):
        if a[i - 1] ** 2 < N <= a[i] ** 2:
            m2 = a[i - 1]
            break
        if a[i - 1] ** 2 < N <= a[i] ** 3:
            m3 = a[i - 1]
        if a[i - 1] ** 4 < N <= a[i] ** 4:
            m4 = a[i - 1]

    res = []
    p = prime(m2 + 1)
    for p4 in range(p.index(m4) + 1):
        for p3 in range(p.index(m3) + 1):
            for p2 in range(len(p)):
                if p[p2] ** 2 + p[p3] ** 3 + p[p4] ** 4 < N:
                    res.append(p[p2] ** 2 + p[p3] ** 3 + p[p4] ** 4)
    print('total number is ', len(set(res)))