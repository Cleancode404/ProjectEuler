"""
Intersections
"""

def cal():
	answer = 0
	digits = tuple(range(10))
	for b in digits:
		for c in digits:
			for d in digits:
				for e in digits:
					for i in digits:
						m = b + c + d - e - i
						if m < 0 or m > 9: continue
						for k in digits:
							f = b + c + d*2 - e - i - k
							if f < 0 or f > 9: continue
							for a in digits:
								for g in digits:
									o = a + b + d - g - k
									if o < 0 or o > 9: continue
									j = a + b + c - g - m
									if j < 0 or j > 9: continue
									l = a + b + c + d - i - j - k
									if l < 0 or l > 9: continue
									h = a + b + c + d - e - f - g
									if h < 0 or h > 9: continue
									n = a + c + d - f - j
									if n < 0 or n > 9: continue
									p = a + b + c - h - l
									if p < 0 or p > 9: continue
									answer += 1
	return str(answer)


if __name__ == "__main__":
	print(cal())