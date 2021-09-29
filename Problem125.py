"""
Palindromic sums

"""

import time

if __name__ == '__main__':
    start = time.process_time()
    N = 100000000
    square = [x ** 2 for x in range(1, int(N ** 0.5) + 1)]
    result = 0
    palindromic = []
    for i in range(len(square)):
        for j in range(i + 2, len(square)):
            s = sum(square[i:j])
            if s >= N:
                break
            if str(s) == str(s)[::-1] and s not in palindromic:
                palindromic.append(s)
                result += s
    print(result)
    print("Runtime is ", time.process_time() - start, "seconds")