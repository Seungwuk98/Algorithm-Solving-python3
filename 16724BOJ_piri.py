n, m = map(int, input().split())
p = []
for i in range(n):
    for j in range(m):
        p.append((i, j))
g = [-1]*(n*m)

mat = [input()for _ in range(n)]
visit = [False]*(n*m)
result = 0
for idx in range(n*m):
    x, y = p[idx]
    q = mat[x][y]
    if q == 'L':
        g[idx] = idx-1
    elif q == 'R':
        g[idx] = idx+1
    elif q == 'U':
        g[idx] = idx-m
    else:
        g[idx] = idx+m
for idx in range(n*m):
    if not visit[idx]:
        now_visit = [idx]
        visit[idx] = True
        next = g[idx]
        while not visit[next]:
            now_visit.append(next)
            visit[next] = True
            next = g[next]
        if next in now_visit:
            result += 1
print(result)
