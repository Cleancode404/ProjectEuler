"""
Exploring the number of different ways 
a number can be expressed as a sum of powers of 2
"""

from Problem171 import cal
import eulerlib, sys


def cal():
	sys.setrecursionlimit(3000)
	NUMBER = 10**25
	ans = count_ways(NUMBER, NUMBER.bit_length() - 1, 2)
	return str(ans)


@eulerlib.memoize
def count_ways(number, exponent, repetitions):
	if exponent < 0:
		return 1 if number == 0 else 0
	else:
		result = count_ways(number, exponent - 1, 2)
		power = 1 << exponent
		upper = power * (repetitions + 2)
		if repetitions > 0 and power <= number < upper:
			result += count_ways(number - power, exponent, repetitions - 1)
		return result


if __name__ == "__main__":
	print(cal())