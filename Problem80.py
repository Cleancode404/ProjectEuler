"""
Square root digital expansion
"""

from decimal import Decimal, getcontext


if __name__ == '__main__':
    getcontext().prec = 102
    answer = 0
    for i in range(1, 101):
        if Decimal(i).sqrt() % 1 != 0:
            answer += sum(int(c) for c in str(Decimal(i).sqrt() * 10 ** 100)[:100])
    print(answer)