n = int(input())
d = 1000000000
dp = [[[0]*(n+1)for _ in range(10)]for _ in range(4)]
for i in range(1, 9):
    dp[0][i][1] = 1
dp[2][9][1] = 1

for i in range(2, n+1):
    dp[1][0][i] = (dp[1][0][i]+dp[0][1][i-1]+dp[1][1][i-1]) % d
    dp[3][0][i] = (dp[3][0][i]+dp[2][1][i-1]+dp[3][1][i-1]) % d
    dp[2][9][i] = (dp[2][9][i]+dp[0][8][i-1]+dp[2][8][i-1]) % d
    dp[3][9][i] = (dp[3][9][i]+dp[1][8][i-1]+dp[3][8][i-1]) % d
    for j in range(1, 9):
        for k in range(0, 4):
            dp[k][j][i] = (dp[k][j][i] + dp[k][j-1][i-1] + dp[k][j+1][i-1]) % d

result = 0
for i in range(10):
    result = (result + dp[3][i][n]) % d
print(result)
