from collections import deque

n, m = map(int, input().split())
order = [[*map(int, input().split())]for _ in range(m)]
g = [[]for _ in range(n+1)]
pointed = [0]*(n+1)
for x in order:
    for i in range(1, len(x)-1):
        g[x[i]].append(x[i+1])
        pointed[x[i+1]] += 1

q = deque()
for i in range(1, n+1):
    if not pointed[i]:
        q.append(i)
result = []
while q:
    now = q.popleft()
    result.append(now)
    for next in g[now]:
        pointed[next] -= 1
        if not pointed[next]:
            q.append(next)

if len(result) != n:
    print(0)
else:
    print('\n'.join(map(str, result)))
