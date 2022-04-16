n, s, m = map(int, input().split())
v = list(map(int, input().split()))
dp = [[-1]*(m+1) for _ in range(n+1)]
dp[0][s] = s

for i in range(1, n+1):
    for j in range(m+1):
        if dp[i-1][j] != -1:
            if j-v[i-1] >= 0:
                dp[i][j-v[i-1]] = j-v[i-1]
            if j+v[i-1] <= m:
                dp[i][j+v[i-1]] = j+v[i-1]


print(max(dp[n]))
