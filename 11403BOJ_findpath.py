import sys
input = sys.stdin.readline

n = int(input())
dp = [[*map(int, input().split())]for _ in range(n)]

for k in range(n):
    for i in range(n):
        for j in range(n):
            if i == k or j == k or dp[i][j]:
                continue
            dp[i][j] = dp[i][k]*dp[k][j]

for x in dp:
    print(*x)
