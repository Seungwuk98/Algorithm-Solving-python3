import sys
input = sys.stdin.readline
n = int(input())
m = int(input())
dp = [[1e9]*(n+1) for _ in range(n+1)]
for i in range(n+1):
    dp[i][i] = 0

for _ in range(m):
    a, b, c = map(int, input().split())
    dp[a][b] = min(dp[a][b], c)

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            if k == i or i == j or j == k:
                continue
            dp[i][j] = min(dp[i][j], dp[i][k]+dp[k][j])

for i in range(1, n+1):
    for j in range(1, n+1):
        if dp[i][j] == 1e9:
            dp[i][j] = 0

for i in range(1, n+1):
    print(*dp[i][1:])
