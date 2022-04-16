from pprint import pprint
n = int(input())
mat = [[0, 0, 0]]+[[*map(int, input().split())]for _ in range(n)]


def sol(mat):
    dp = [[0]*3 for _ in range(n+1)]
    for i in range(1, n+1):
        j, k = 1, 2
        for w in range(3):
            dp[i][w] = min(dp[i-1][j], dp[i-1][k])+mat[i][w]
            j, k = (j+1) % 3, (k+1) % 3
    return dp


r = 1e9
j, k = 1, 2
for i in range(3):
    tmp1, tmp2 = mat[1][j], mat[1][k]
    mat[1][j], mat[1][k] = [int(1e9)]*2
    dp = sol(mat)
    r = min(r, min(dp[-1][j], dp[-1][k]))
    mat[1][j], mat[1][k] = tmp1, tmp2
    j, k = (j+1) % 3, (k+1) % 3
print(r)
