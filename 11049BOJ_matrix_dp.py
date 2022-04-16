import sys
input = sys.stdin.readline

n = int(input())
mat = [[0, 0]] + [[*map(int, input().split())]for _ in range(n)]
dp = [[1e9]*(n+1) for _ in range(n+1)]
dp[1] = [0]*(n+1)

for i in range(1, n+1):
    for j in range(i, n+1):
        for k in range(1, i):
            dp[i][j] = min(dp[i][j], dp[i-k][j-k]+dp[k][j]+mat[j-i+1]
                           [0]*mat[j-k][1]*mat[j][1])
print(dp[n][n])
