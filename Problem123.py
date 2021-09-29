"""
Prime square remainders

"""

import time



import time
from pe069 import prime_sieve

if __name__ == '__main__':
    start = time.process_time()
    prime = prime_sieve(300000)
    for i in range(0, len(prime), 2):
        if 2 * (i + 1) * prime[i] % prime[i] ** 2 > 10000000000:
            print(i + 1)
            break
    print('Runtime is', time.process_time() - start)