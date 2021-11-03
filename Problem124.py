"""
Ordered radicals

"""

def compute(x):
    limit = 100000

    rads = [0] + [1]* limit
    for i in range(2, len(rads)):
        if rads[i] == 1:
            for j in range(i, len(rads), i):
                rads[j] *= i

    data = sorted((rads, i) for (i, rad) in enumerate(rads))
    return str(data[1000][1])


if __name__ =="__main__":
    print(compute(10000))