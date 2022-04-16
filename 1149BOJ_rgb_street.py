import sys
input = sys.stdin.readline

n = int(input())
rgb = [[*map(int, input().split())]for _ in range(n)]
dp = [[0]*3 for _ in range(n+1)]
for i in range(1, n+1):
    for j in range(3):
        dp[i][j] = min(dp[i-1][(j+1) % 3], dp[i-1][(j+2) % 3])+rgb[i-1][j-1]
print(min(dp[-1]))
