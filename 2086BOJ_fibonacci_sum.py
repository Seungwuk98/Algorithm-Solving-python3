a, b = map(int, input().split())
d = 1000000000


def mat_cross(mat1, mat2):
    r = [[0, 0], [0, 0]]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                r[i][j] = (r[i][j] + (mat1[i][k]*mat2[k][j]) % d) % d
    return r


def mat_pow(n, mat):
    r = [[1, 0], [0, 1]]
    c = mat
    while n:
        if n & 1:
            r = mat_cross(r, c)
        c = mat_cross(c, c)
        n >>= 1
    return r


m = mat_pow(a, [[1, 1], [1, 0]])
f_a = m[0][0]
m = mat_pow(b+1, [[1, 1], [1, 0]])
f_b = m[0][0]
print((f_b - f_a) % d)
