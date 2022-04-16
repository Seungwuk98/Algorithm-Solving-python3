g = [*map(int, input().split())]
dp = [[[1000000]*5 for __ in range(5)] for _ in range(len(g)-1)]
ddr = [1, 2, 3, 4]
qry = g[0]
dp[0][qry][0] = 2
dp[0][0][qry] = 2
l = len(g)


def move(i, j):
    if not i:
        return 2
    elif i == j:
        return 1
    idxi = ddr.index(i)
    idxj = ddr.index(j)
    if abs(idxj-idxi) & 1:
        return 3
    else:
        return 4


for i in range(1, l-1):
    q = g[i]
    for j in range(5):
        if q != j:
            for k in range(5):
                if k != q and j:
                    dp[i][j][q] = min(dp[i][j][q], dp[i-1][k][q]+move(k, j))
                    dp[i][q][j] = min(dp[i][q][j], dp[i-1][q][k]+move(k, j))
                if j != k:
                    dp[i][j][q] = min(dp[i][j][q], dp[i-1][j][k]+move(k, q))
                    dp[i][q][j] = min(dp[i][q][j], dp[i-1][k][j]+move(k, q))
print(min([min(x) for x in dp[-1]]))
