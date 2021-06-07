"""
digit factorial chains
"""

factorial = [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]

def next_number(n):
    factorial_sum = 0
    while n != 0:
        factorial_sum += factorial[n % 10]
        n //= 10
    return factorial_sum

def chain_len(n):
    chain = []
    while not chain.__contains__(n):
        chain.append(n)
        n = next_number(n)
    return len(chain)

if __name__ == '__main__':
    result = 0
    for i in range(1000000):
        if chain_len(i) == 60:
            result += 1
    print(result)