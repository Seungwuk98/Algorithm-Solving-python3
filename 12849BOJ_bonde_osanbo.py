from pprint import pprint
d = int(input())
graph = [[1, 2], [0, 2, 3], [0, 1, 3, 4], [1, 2, 4, 5],
         [2, 3, 5, 7], [3, 4, 6], [5, 7], [4, 6]]

dp = [1]+[0]*7
for _ in range(d):
    tmp = [0]*8
    for i in range(8):
        for k in graph[i]:
            tmp[i] += dp[k]
            tmp[i] %= 1000000007
    dp = tmp
print(dp[0])


dp = [[0]*(d+1)for _ in range(8)]
dp[0][0] = 1
for j in range(1, d+1):
    for i in range(8):
        for k in graph[i]:
            if dp[k][j-1] != 0:
                dp[i][j] += dp[k][j-1]
pprint(dp)
print(dp[0][d] % 1000000007)
