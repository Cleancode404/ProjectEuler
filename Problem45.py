#triangular, pentagonal, and hexagonal

"""
Triangle, pentagonal, and hexagonal numbers are generated
 by the following formulae:
Triangle 	  	Tn=n(n+1)/2 	  	1, 3, 6, 10, 15, ...
Pentagonal 	  	Pn=n(3n−1)/2 	  	1, 5, 12, 22, 35, ...
Hexagonal 	  	Hn=n(2n−1) 	  	1, 6, 15, 28, 45, ...

It can be verified that T285 = P165 = H143 = 40755.

Find the next triangle number that is also pentagonal and hexagonal.

"""""
import time 

def project_euler():
    p, h = 165, 144
    hen = set()
    next_pen = next_hen = 0
    while next_pen not in hen:
        next_pen = p * (3 * p - 1) // 2
        p += 1
        while next_hen < next_pen:
            h += 1
            next_hen = h * (2 * h - 1)
            hen.add(next_hen)
    return next_hen

if __name__ == '__main__':
    start = time.clock()
    print(project_euler())
    print('Runtime is ', time.clock() - start)