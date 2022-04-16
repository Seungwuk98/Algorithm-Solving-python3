from copy import deepcopy
from pprint import pprint
n, m = map(int, input().split())
arr = [[0]*(m+1)]+[[0]+[*map(int, [*input()])]for _ in range(n)]
dp = [[0]*(m+1)for _ in range(n+1)]
for i in range(1, n+1):
    for j in range(1, m+1):
        if arr[i][j] == 1:
            dp[i][j] = min(dp[i-1][j], dp[i-1][j-1], dp[i][j-1])+1
        else:
            dp[i][j] = 0

pprint(dp)


def max_value(data):
    return max([max(x) for x in data])


print(max_value(dp)**2)
