n, m = map(int, input().split())
m_arr = [*map(int, input().split())]
c_arr = [*map(int, input().split())]
cost = sum(c_arr)
dp = [[0]*(cost+1) for _ in range(n+1)]
for i in range(n):
    w, v = m_arr[i], c_arr[i]
    for j in range(v):
        dp[i+1][j] = dp[i][j]
    for j in range(v, cost+1):
        dp[i+1][j] = max(dp[i][j-v]+w, dp[i][j])
min_cost = 1e9

for i in range(cost+1):
    if dp[-1][i] >= m:
        min_cost = min(min_cost, i)
print(min_cost)
