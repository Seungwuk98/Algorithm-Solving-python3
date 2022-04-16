import sys
input = sys.stdin.readline
print = sys.stdout.write

a = input().rstrip()
b = input().rstrip()
dp = [[0]*(len(a)+1) for _ in range(len(b)+1)]

for i in range(1, len(b)+1):
    for j in range(1, len(a)+1):
        if b[i-1] == a[j-1]:
            dp[i][j] = dp[i-1][j-1]+1
        else:
            dp[i][j] = max(dp[i][j-1], dp[i-1][j])

print(str(max(sum(dp, []))))
