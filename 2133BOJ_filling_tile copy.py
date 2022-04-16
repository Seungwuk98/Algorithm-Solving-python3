t = int(input())
if t & 1:
    print(0)
    exit(0)
if t == 0:
    print(1)
    exit(0)
elif t == 2:
    print(3)
    exit(0)
t //= 2


def mat_cross(mat1, mat2):
    result = [[0]*2 for _ in range(2)]
    for i in range(2):
        for j in range(2):
            result[i][j] = (mat1[i][0]*mat2[0][j] + mat1[i]
                            [1]*mat2[1][j]) % 1000000007
    return result


def mat_pow(mat, N):
    if N == 1:
        return mat
    result = [[1, 0], [0, 1]]
    while N:
        if N & 1:
            result = mat_cross(result, mat)
        mat = mat_cross(mat, mat)
        N >>= 1
    return result


mat = mat_pow([[4, -1], [1, 0]], t-1)
print(((mat[0][0]*3) % 1000000007+(mat[0][1]*1) % 1000000007) % 1000000007)
