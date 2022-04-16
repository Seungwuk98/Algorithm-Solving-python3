n, m = map(int, input().split())
lad = {}
for _ in range(n+m):
    a, b = map(int, input().split())
    lad[a] = b

dp = [False]*101
dp[1] = True
idx = set([1])
count = 0
while not dp[100]:
    tmp = set([])
    for i in idx:
        for di in range(1, 7):
            ni = i+di
            if ni > 100 or dp[ni]:
                continue
            dp[ni] = True
            if ni in lad:
                ni = lad[ni]
                dp[ni] = True
            tmp.add(ni)

    idx = tmp
    count += 1
print(count)
