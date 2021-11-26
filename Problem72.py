"""
counting fractions
"""

import time
from pe070 import totient_array


if __name__ == '__main__':
    start = time.clock_gettime()
    N = 1000000
    print(sum(totient_array(N)) - 1)
    print('Runtime is ', time.clock_gettime() - start)