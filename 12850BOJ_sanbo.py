d = 1000000007


def mat_cross(mat1, mat2):
    r = [[0]*8 for _ in range(8)]

    for i in range(8):
        for j in range(8):
            for k in range(8):
                r[i][j] = (r[i][j] + (mat1[i][k]*mat2[k][j]) % d) % d

    return r


def mat_pow(mat, n):
    r = [[0]*8 for _ in range(8)]
    for i in range(8):
        r[i][i] = 1
    c = mat
    while n:
        if n & 1:
            r = mat_cross(r, c)

        c = mat_cross(c, c)
        n >>= 1
    return r


mat = [
    [0, 1, 1, 0, 0, 0, 0, 0],
    [1, 0, 1, 1, 0, 0, 0, 0],
    [1, 1, 0, 1, 1, 0, 0, 0],
    [0, 1, 1, 0, 1, 1, 0, 0],
    [0, 0, 1, 1, 0, 1, 1, 0],
    [0, 0, 0, 1, 1, 0, 0, 1],
    [0, 0, 0, 0, 1, 0, 0, 1],
    [0, 0, 0, 0, 0, 1, 1, 0]
]
D = int(input())
c = mat_pow(mat, D)
print(c[0][0])
