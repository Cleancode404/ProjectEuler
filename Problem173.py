"""
Using up to one million tiles 
how many different "hollow" square laminae can be formed?
"""

def cal():
	TILES = 10**6
	answer = 0
	for n in range(3, TILES // 4 + 2):  # Outer square length
		for k in range(n - 2, 0, -2):  # Inner square length
			if n * n - k * k > TILES:
				break
			answer += 1
	return str(answer)


if __name__ == "__main__":
	print(cal())