n = int(input())
dp = [False] * (n+1)
dp[n] = True
idx = [n]
count = 0

while not dp[1]:
    tmp = []
    for i in idx:
        if i % 3 == 0 and not dp[i//3]:
            dp[i//3] = True
            tmp.append(i//3)
        if i % 2 == 0 and not dp[i//2]:
            dp[i//2] = True
            tmp.append(i//2)
        if i-1 >= 1 and not dp[i-1]:
            dp[i-1] = True
            tmp.append(i-1)
    idx = tmp
    count += 1
print(count)
