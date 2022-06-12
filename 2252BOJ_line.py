n, m = map(int, input().split())
g = [[]for _ in [0]*(n+1)]
v = [0]*(n+1)
while m:
    a, b = map(int, input().split())
    g[b].append(a)
    m -= 1


def dfs(x):
    v[x] = 1
    for t in g[x]:
        if not v[t]:
            dfs(t)
    print(x, end=" ")


for i in range(1, n+1):
    if not v[i]:
        dfs(i)
