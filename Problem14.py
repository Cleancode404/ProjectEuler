#Longest Collatz sequence
# Which starting number, under one million, produces the longest chain?#

import time
start = time.time()

n = 13
max_length = [0, 0]
ipo = 0

# def collatz_sequence(n):
def collatz_sequence(n):
    counter = 0 
    while n > 1:
        if n%2 == 0:
            n = n//2
            counter += 1
        else:
            n = 3*n + 1
            counter += 1
    return counter

for i in range(1000000):
    ipo = collatz_sequence(i)
    if ipo > max_length[0]:
        max_length[0] = ipo
        max_length[1] = i
print(max_length)

end  = time.time()

print (end - start)
