#Longest Collatz sequence
# Which starting number, under one million, produces the longest chain?#

def collatz_sequence(n):
    counter = 0 
    while n > 1:
        if n%2 == 0:
            n = n//2
            i = i + 1
        else:
            n = 3*n + 1
            i = i + 1
    return i, n 


print(collatz_sequence(90123))
