n, s = map(int, input().split())

dp = [[False]*1001 for _ in range(51)]
comb = [0]*51
for i in range(2, 51):
    comb[i] = i*(i-1)//2
for i in range(3, 51):
    if comb[i-1] < 1001:
        dp[i][comb[i-1]] = True


for i in range(3, 51):
    for j in range(1, 1001):
        if dp[i][j]:
            for k in range(i+1, 51):
                w = k-i
                if j+comb[w+1] < 1001:
                    dp[k][j+comb[w+1]] = True

print(+dp[n][s])
