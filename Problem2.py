# Each new term in the Fibonacci sequence is generated
#  by adding the previous two terms. 
#By starting with 1 and 2, the first 10 terms will be:

#1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

#By considering the terms in the Fibonacci sequence whose values 
# do not exceed four million, find the sum of the even-valued terms.
#


#create fibonacci sequence function with recurssion but it is too slow

# def fibonacci_seq(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return fibonacci_seq(n-2) + fibonacci_seq(n-1)

# print(fibonacci_seq(6))
a, b, c = 1, 1, 0
sum = 0
while c < 4000000:
    c = a + b
    if c %2 == 0:
        sum = sum + c

    a =b
    b = c 

print(sum)