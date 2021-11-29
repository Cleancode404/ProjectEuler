"""
Passcode derivation
"""


if __name__ == '__main__':
    after = [set() for x in range(10)]
    before = [set() for x in range(10)]

    f = open('pe079.txt')
    for line in f:
        num = line[0:3]
        for i in range(0, 2):
            for j in range(i + 1, 3):
                after[int(num[i])].add(int(num[j]))
                before[int(num[j])].add(int(num[i]))
    for i in range(10):
        print('after', i, ':', after[i])
    print('=================================')
    for i in range(10):
        print('before', i, ':', before[i])