#The sequence of triangle numbers is generated by adding the natural numbers. 
# So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. 
# The first ten terms would be:
# 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

# What is the value of the first triangle number to have
#  over five hundred divisors?#

import time 

def number_of_divisors(n):
    divisors = 1
    count = 0
    while n % 2 == 0:
        count += 1
        n //= 2
    divisors *= (count + 1)
    p = 3
    while n != 1:
        count = 0
        while n % p == 0:
            count += 1
            n //= p
        divisors *= (count + 1)
        p += 2
    return divisors


if __name__ == '__main__':
    start = time.process_time()
    i = 1
    while number_of_divisors(i * (i + 1) // 2) <= 500:
        i += 1
    print(i * (i + 1) // 2,'\n','Runtime is', time.process_time() - start)