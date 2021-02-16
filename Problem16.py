#Power digit sum#

#2**15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
# What is the sum of the digits of the number 2**1000?#

import time
#find out how long it will take to compute
start = time.time()

def sum_digit(n):
    sum = 0
    while n >= 1:
        n, reminder = n//10, n%10
        sum = sum + reminder
    return sum

print(sum_digit(2**1000))


end  = time.time()

print (end - start)