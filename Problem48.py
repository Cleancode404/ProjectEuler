#self powers
"""

The series, 1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317.

Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1^0001000.

"""""

if __name__ == '__main__':
    answer = 0
    for i in range(1, 1001):
        answer += i ** i
    print(answer % (10 ** 10))