n = int(input())
d = [[0, 0]]+[[*map(int, input().split())]for _ in range(n)]
dp = [0]*(n+1)

for i in range(1, n+1):
    day, pay = d[i]
    if i+day-1 > n:
        continue
    dp[i+day-1] = max(dp[i+day-1], max(dp[:i])+pay)
print(max(dp))

dp = [0]*(n+1)+[0]
for i in range(n, 0, -1):
    day, pay = d[i]
    if i+day-1 > n:
        continue
    dp[i] = max(dp[i+day:])+pay
print(max(dp))
