from pprint import pprint
n, m = map(int, input().split())
A = [[*map(int, [*input()])]for _ in range(n)]
B = [[*map(int, [*input()])]for _ in range(n)]


def flip(mat, i, j):
    for k in range(i, i+3):
        for l in range(j, j+3):
            mat[k][l] ^= 1


if A == B:
    print(0)
else:
    count = 0
    for i in range(n-2):
        for j in range(m-2):
            if A[i][j] != B[i][j]:
                flip(A, i, j)
                count += 1
            if A == B:
                print(count)
                exit(0)
    print(-1)
