from pprint import pprint
n = int(input())
s = [0]+[int(input())for _ in range(n)]
dp = [[-1]*(n+1)for _ in range(n+1)]
dp[0][1] = 0
dp[1][1] = s[1]
if n >= 2:
    dp[2][1] = s[2]+s[1]
for i in range(2, n+1):
    dp[i][i] = max(dp[i-2]) + s[i]
    if i+1 <= n:
        dp[i+1][i] = dp[i][i]+s[i+1]
pprint(max(dp[-1]))
