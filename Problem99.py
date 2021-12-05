"""
Largest exponential
"""

import math

if __name__ == '__main__':
	max_value = 525806 * math.log(519432)
	count = 0
	answer = 1
	f = open('pe099.txt')
	for line in f:
		count += 1
		number = [int(x) for x in line.split(',')]
		if max_value < number[1] * math.log(number[0]):
			answer = count
			max_value = number[1] * math.log(number[0])
	print(answer)