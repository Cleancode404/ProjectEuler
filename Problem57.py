
if __name__ == 'main':
    numerator, denominator, count, K = 1, 1, 0, 1000
    for i in range(K):
        numberator, denominator = numerator + 2 * denominator, numerator + denominator
        if len(str(numerator)) > len(str(denominator)):
            count += 1
    print(count)
