n, s, e, t = map(int, input().split())
road = [[*map(int, [*input()])]for _ in range(n)]
D = 1000003


def rotate(mat):
    ret = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            ret[i][j] = road[j][i]
    return ret


def mat_cross(mat1, mat2):
    ret = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                ret[i][j] += mat1[i][k] * mat2[k][j]
                ret[i][j] %= D
    return ret


def mat_pow(mat, n):
    ret = [[0]for _ in range(n)]
    for i in range(n):
        ret[i][i] = 1
    while n:
        if n & 1:
            ret = mat_cross(ret, mat)
        mat = mat_cross(mat, mat)
        n >>= 1
    return ret


ret = rotate(road)

mat = [[[0]*n for _ in range(n)]for _ in range(5)]

for i in range(5):
    for j in range(n):
        for k in range(n):
            if ret[j][k]:
                mat[i][j][k] = 0 if (i+1) % ret[j][k] else 1

total = [[0]*n for _ in range(n)]
for i in range(n):
    total[i][i] = 1
for i in range(5):
    total = mat_cross(total, mat[i])
print(total)

m = 1
while m*5 < t:
    m *= 5
