#Goldbach's other conjecture

"""


It was proposed by Christian Goldbach that every odd composite number
 can be written as the sum of a prime and twice a square.

9 = 7 + 2×12
15 = 7 + 2×22
21 = 3 + 2×32
25 = 7 + 2×32
27 = 19 + 2×22
33 = 31 + 2×12

It turns out that the conjecture was false.

What is the smallest odd composite that cannot be
 written as the sum of a prime and twice a square?

"""""



def is_prime(n):
    if n < 2:
        return False
    if n % 2 == 0 or n % 3 == 0 or n % 5 == 0:
        return n == 2 or n == 3 or n == 5
    return all(n % i != 0 for i in range(7, int(n ** 0.5) + 1, 2))

def is_prime_1(n):
    return not (n < 2 or any(n % i == 0 for i in range(2, int(n ** 0.5) + 1)))

def is_go_other_con(n):
    return any(is_prime(n - 2 * i * i) for i in range(int((n / 2) ** 0.5) + 1))

if __name__ == '__main__':
    k = 33
    while is_go_other_con(k):
        k += 2
    print(k)