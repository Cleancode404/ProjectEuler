"""

Prime cube partnership

"""

primes = []

is_prime = [True for i in range(1000000)]
for i in range(2, len(is_prime)):
	if is_prime[i]:
		primes.append(i)
		for j in range(i+i, len(is_prime), i):
			is_prime[j] = False

prime_set = set(primes)

count = 0

for k in range(1, 1000):
	q = k*3*(k+1) + 1
	if q in prime_set:
		count += 1
print(count)