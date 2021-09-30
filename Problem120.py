"""
Square remainders

"""

if __name__ == '__main__':
    result = 0
    for i in range(3, 1001):
        result += i * i - i
        if i % 2 == 0:
            result -= i
    print(result)