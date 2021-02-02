#
# Find the difference between the sum of the squares of the first one hundred natural numbers
#  and the square of the sum.#

def square_sum(n):
    sum1 = 0
    for i in range(n):
        sum1 = sum1 + i*i
    return sum1

print(square_sum(101))

def sum_square(n):
    sum2 = 0
    for j in range(n):
        sum2 = sum2 + j
    return sum2*sum2


print(sum_square(101) - square_sum(101))
