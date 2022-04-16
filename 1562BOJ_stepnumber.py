n = int(input())
d = 1000000000
dp = [[[0]*(n+1)for _ in range(10)]for _ in range(1 << 10)]
for i in range(1, 10):
    dp[1 << i][i][1] = 1

for i in range(2, n+1):
    for k in range(1, 1 << 10):
        for j in range(10):
            if k & (1 << j):
                for x in (j-1, j+1):
                    if 0 <= x < 10:
                        dp[k][j][i] = ((
                            (dp[k][j][i]+dp[k & ~(1 << j)][x][i-1]) % d)+dp[k][x][i-1]) % d

result = 0
for i in range(10):
    result = (result + dp[(1 << 10)-1][i][n]) % d
print(result)
