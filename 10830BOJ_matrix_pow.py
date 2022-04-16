n, b = map(int, input().split())
mat = [[*map(int, input().split())]for _ in range(n)]
d = 1000


def mat_cross(n, A, B):
    C = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                C[i][j] = (C[i][j] + (A[i][k]*B[k][j]) % d) % d
    return C


def mat_pow(n, x, A):
    r = [[0]*n for _ in range(n)]
    for i in range(n):
        r[i][i] = 1
    while x:
        if x & 1:
            r = mat_cross(n, r, A)
        A = mat_cross(n, A, A)
        x >>= 1
    return r


result = mat_pow(n, b, mat)
for y in result:
    print(*y)
