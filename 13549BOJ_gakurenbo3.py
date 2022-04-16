n, k = map(int, input().split())

dp = [False]*100001
idx = []


def teleport(tmp, dp, n):
    x = n
    while x < 100001:
        if dp[x]:
            break
        tmp.append(x)
        dp[x] = True
        x *= 2


teleport(idx, dp, n)
count = 0
while not dp[k]:
    tmp = []
    for i in idx:
        if i-1 >= 0 and not dp[i-1]:
            teleport(tmp, dp, i-1)
        if i+1 <= 100000 and not dp[i+1]:
            teleport(tmp, dp, i+1)
    idx = tmp
    count += 1
print(count)
