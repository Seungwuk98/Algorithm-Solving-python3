import sys
input = sys.stdin.readline

n = int(input())
g = [[]for _ in range(n+1)]
visit = [False]*(n+1)
for _ in range(n-1):
    a, b = map(int, input().split())
    g[a].append(b)
    g[b].append(a)

depth = [0]*(n+1)
parent = [0]*(n+1)
bfs = [*map(int, input().split())]
s = 1
q = deque([s])
visit[s] = True
while q:
    now = q.popleft()
    for next in g[now]:
        if not visit[next]:
            visit[next] = True
            depth[next] = depth[now]+1
            parent[next] = now
            q.append(next)

now = 0
sort = [[]for _ in range(100001)]
sort[0].append(s)
pr = 0
for i in range(1, n):
    if depth[s] != depth[bfs[i]]:
        now += 1
        pr = 0
    if depth[bfs[i]] != now:
        print(0)
        exit(0)
    try:
        while sort[now-1][pr] != parent[bfs[i]]:
            pr += 1
    except:
        print(0)
        exit(0)
    sort[now].append(bfs[i])
    s = bfs[i]
print(1)
