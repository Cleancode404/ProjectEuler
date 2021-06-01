"""
Pandigital Fibonacci ends
"""

import time


def is_pandigital(n):
	return sorted(str(n)) == ['1', '2', '3', '4', '5', '6', '7', '8', '9']

def head_digits(n):
	t = n * 0.20898764024997873 - 0.3494850021680094
	t = int(pow(10, t - int(t) + 8))
	return t

if __name__ == '__main__':
	start = time.clock()
	k = 2
	f1 = 1
	f2 = 1
	while not is_pandigital(f2) or not is_pandigital(head_digits(k)):
		k += 1
		f1, f2 = f2, (f1 + f2) % 1000000000
	print(k)
	print('Runtime is', time.clock() - start)