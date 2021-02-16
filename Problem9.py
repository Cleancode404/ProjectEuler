#Special Pythagorean triplet#
"""
A Pythagorean triplet is a set of three natural numbers, 
a < b < c, for which,
a^2 + b^2 = c^2
For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""

#since a < b < c and a + b + c = 1000
#stop at 400 to save time

for a in range(1, 400):
    for b in range(1, 400):
        c = (1000 - a) -b
        if a < b < c:
            #pythagorean theorem
            if a**2 + b**2  == c**2:
                #check output
                print(a, b, c)
                print(a*b*c)