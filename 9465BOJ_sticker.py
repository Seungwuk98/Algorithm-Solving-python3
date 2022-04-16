from heapq import *
import sys
input = sys.stdin.readline
for _ in range(int(input())):
    n = int(input())
    m = [[0]+[*map(int, input().split())]for _ in range(2)]
    dp = [[0]*(n+1) for _ in range(2)]
    dp[0][1] = m[0][1]
    dp[1][1] = m[1][1]
    for j in range(2, n+1):
        for i in range(2):
            dp[i][j] = max(dp[(i+1) % 2][j-1], dp[(i+1) % 2][j-2])+m[i][j]
    print(max(dp[0][-1], dp[1][-1]))
