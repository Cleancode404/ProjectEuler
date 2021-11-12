"""
abc-hits
"""
import math
def cal():
	LIMIT = 120000
	
	# Modification of the sieve of Eratosthenes
	rads = [0] + [1] * (LIMIT - 1)
	for i in range(2, len(rads)):
		if rads[i] == 1:
			for j in range(i, len(rads), i):
				rads[j] *= i
	
	sortedrads = sorted((rad, n) for (n, rad) in enumerate(rads))
	sortedrads = sortedrads[1 : ]  # Get rid of the (0, 0) entry
	
	ans = 0
	for c in range(2, LIMIT):
		for (rad, a) in sortedrads:
			rad *= rads[c]
			if rad >= c:
				break
			b = c - a
			if a < b and rad * rads[b] < c and math.gcd(a, b) == 1:
				ans += c
	return str(ans)


if __name__ == "__main__":
	print(cal())