
n = int(input())
mat = [[*map(int, input().split())]for _ in range(n)]
dp = [[[0, 0, 0]for _ in range(n)]for _ in range(n)]
dp[0][1][0] = 1

for i in range(n):
    for j in range(1, n):
        if i == 0 and j == 1:
            continue
        if mat[i][j]:
            continue
        dp[i][j][0] = dp[i][j-1][0]+dp[i][j-1][1]
        if i >= 1:
            if not mat[i-1][j] and not mat[i][j-1]:
                dp[i][j][1] = sum(dp[i-1][j-1])
            dp[i][j][2] = dp[i-1][j][1]+dp[i-1][j][2]
print(sum(dp[-1][-1]))
