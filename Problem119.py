"""
Digit power sum

"""
import time

def digit_sum(n):
    return sum(map(int, str(n)))

if __name__ == '__main__':
    start = time.process_time()
    array = []
    for base in range(2, 100):
        for e in range(2, 30):
            p = base ** e
            if digit_sum(p) == base:
                array.append(p)
    print(sorted(array)[29])
    print("Runtime is", time.process_time() - start, "seconds")