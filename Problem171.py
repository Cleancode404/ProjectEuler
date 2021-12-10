"""
Finding numbers for which the sum of the squares of the digits is a square
"""

import eulerlib, itertools

def cal():
	LENGTH = 20
	BASE = 10
	MODULUS = 10**9
	
	# Maximum possible squared digit sum (for 99...99)
	MAX_SQR_DIGIT_SUM = (BASE - 1)**2 * LENGTH
	
	# sqsum[n][s] is the sum of all length-n numbers with a square digit sum of s, modulo MODULUS
	# count[n][s] is the count of all length-n numbers with a square digit sum of s, modulo MODULUS
	sqsum = []
	count = []
	
	for i in range(LENGTH + 1):
		sqsum.append([0] * (MAX_SQR_DIGIT_SUM + 1))
		count.append([0] * (MAX_SQR_DIGIT_SUM + 1))
		if i == 0:
			count[0][0] = 1
		else:
			for j in range(BASE):
				for k in itertools.count():
					index = k + j**2
					if index > MAX_SQR_DIGIT_SUM:
						break
					sqsum[i][index] = (sqsum[i][index] + sqsum[i - 1][k] + pow(BASE, i - 1, MODULUS) * j * count[i - 1][k]) % MODULUS
					count[i][index] = (count[i][index] + count[i - 1][k]) % MODULUS
	
	ans = sum(sqsum[LENGTH][i**2] for i in range(1, eulerlib.sqrt(MAX_SQR_DIGIT_SUM)))
	return f"{ans%MODULUS:09}"


if __name__ == "__main__":
	print(cal())