"""
Triangle containment
"""


if __name__ == '__main__':
    count = 0
    f = open('pe102.txt')
    for line in f:
        triangles = [int(x) for x in line.split(',')]
        nu = triangles[4] * triangles[1] - triangles[0] * triangles[5]
        nv = triangles[0] * triangles[3] - triangles[2] * triangles[1]
        denominator = (triangles[2] - triangles[0]) * (triangles[5] - triangles[1]) - (triangles[4] - triangles[0]) * (triangles[3] - triangles[1])
        if nu / denominator > 0 and nv / denominator > 0 and (nu + nv) / denominator < 1:
            count += 1
    print(count)