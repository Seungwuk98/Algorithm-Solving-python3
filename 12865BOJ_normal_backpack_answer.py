from copy import deepcopy
n, k = map(int, input().split())
t = [[0, 0]]
for w, v in [[*map(int, input().split())]for _ in range(n)]:
    if w > k:
        continue
    t.append([w, v])
dp = [0]*(k+1)
for w, v in t:
    tmp = deepcopy(dp)
    for i in range(w, k+1):
        tmp[i] = max(tmp[i], dp[i-w]+v)
    dp = tmp
print(max(dp))
