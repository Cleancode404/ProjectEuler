#Euler project question 1
# If we list all the natural numbers below 10 that are 
# multiples of 3 or 5, we get 3, 5, 6 and 9. 
# The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.
#

def accumulate_sum(n):
    i = 0
    sum = 0
    while i < n:
        if n%3 == 0 or n%5 == 0:
            sum = sum + n
            n = n - 1
        else:
            n = n - 1
    return sum 

print(accumulate_sum(10-1))
print(accumulate_sum(1000-1))