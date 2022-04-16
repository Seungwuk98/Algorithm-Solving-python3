import sys
input = sys.stdin.readline
n, m = map(int, input().split())
dp = [[1e9]*(n+1) for _ in range(n+1)]
for i in range(n+1):
    dp[i][i] = 0
for _ in range(m):
    a, b = map(int, input().split())
    dp[a][b] = 1
    dp[b][a] = 1

for i in range(1, n+1):
    for j in range(1, n+1):
        for k in range(1, n+1):
            if j == i or k == i or j == k:
                continue
            dp[j][k] = min(dp[j][i]+dp[i][k], dp[j][k])
min_value = 1e9
min_idx = -1
for x in range(1, n+1):
    s = sum(dp[x][1:])
    if s < min_value:
        min_value = s
        min_idx = x
print(min_idx)
