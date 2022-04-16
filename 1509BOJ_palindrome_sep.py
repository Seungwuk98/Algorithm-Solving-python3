import sys
input = sys.stdin.readline

s = input().rstrip()
l = len(s)
dp = [[False]*l for _ in range(l)]
for i in range(l):
    dp[i][i] = True
for i in range(l-1):
    if s[i] == s[i+1]:
        dp[i][i+1] = True

for j in range(3, l+1):
    for k in range(l-j+1):
        if s[k] == s[k+j-1]:
            if dp[k+1][k+j-2]:
                dp[k][k+j-1] = True
dp2 = [10000]*l
for j in range(l):
    for i in range(j+1):
        if dp[i][j]:
            if i == 0:
                dp2[j] = 1
            else:
                dp2[j] = min(dp2[j], dp2[i-1] + 1)
print(dp2[-1])
