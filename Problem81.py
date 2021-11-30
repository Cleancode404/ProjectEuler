"""
Path sum: two ways

"""


if __name__ == '__main__':
    matrix = []
    f = open('pe081.txt')
    for line in f:
        matrix.append([int(x) for x in line.split(',')])
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if i == 0 and j == 0:
                continue
            elif i == 0:
                matrix[i][j] += matrix[i][j - 1]
            elif j == 0:
                matrix[i][j] += matrix[i - 1][j]
            else:
                matrix[i][j] += min(matrix[i][j - 1], matrix[i - 1][j])
    print(matrix[len(matrix) - 1][len(matrix[0]) - 1])