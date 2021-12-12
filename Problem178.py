"""
Step Numbers
"""

import eulerlib


def cal():
	LIMIT = 40
	answer = sum(count_step_pandigital(digits, head, 0, 9)
		for digits in range(LIMIT + 1)
		for head in range(1, 10))
	return str(answer)

@eulerlib.memoize
def count_step_pandigital(digits, head, low, high):
	assert digits >= 0
	assert low <= head <= high
	if digits <= 1:
		return 1 if (low == head == high) else 0
	else:
		result = 0
		if head - 1 >= low:
			result += count_step_pandigital(digits - 1, head - 1, low, high)
			if head == high:
				result += count_step_pandigital(digits - 1, head - 1, low, high - 1)
		if head + 1 <= high:
			result += count_step_pandigital(digits - 1, head + 1, low, high)
			if head == low:
				result += count_step_pandigital(digits - 1, head + 1, low + 1, high)
		assert 0 <= result < 10**digits
		return result


if __name__ == "__main__":
	print(cal())