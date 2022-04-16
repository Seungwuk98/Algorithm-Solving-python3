import sys
input = sys.stdin.readline
for _ in range(int(input())):
    k = int(input())
    files = [0]+[*map(int, input().split())]
    for i in range(1, k+1):
        files[i] += files[i-1]
    dp = [[0]*(k+1)for _ in range(k+1)]

    for p in range(1, k):
        for i in range(1, k+1-p):
            dp[i][i+p] = min([dp[i][j] + dp[j+1][i+p]
                             for j in range(i, i+p)]) + files[i+p]-files[i-1]
    print(dp[1][k])
