n = int(input())
a = [*map(int, input().split())]
dp = [False]*40001
dp[0] = True
for i in range(n):
    for j in range(40000, a[i]-1, -1):
        dp[j] = dp[j] or dp[j-a[i]]
for i in range(n):
    for j in range(0, 40001-a[i]):
        dp[j] = dp[j] or dp[j+a[i]]

m = int(input())
for x in map(int, input().split()):
    print('Y' if dp[x] else 'N', end=' ')
