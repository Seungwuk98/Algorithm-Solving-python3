import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

n = int(input())
g = [[]for _ in range(n+1)]
for _ in range(n-1):
    a, b, c = map(int, input().split())
    g[a].append((c, b))
    g[b].append((c, a))

trip = []
f_app = [0]*(n+1)
depth = [0]*(n+1)
visit = [False]*(n+1)
visit[1] = True


def dfs(node, level):
    f_app[node] = len(trip)
    depth[node] = level
    trip.append(node)
    for next_dist, next in g[node]:
        if not visit[next]:
            visit[next] = True
            dfs(next, level+next_dist)
            trip.append(node)


def find_lca(a, b):
    x, y = f_app[a], f_app[b]
    if x > y:
        x, y = y, x
    _min = 1e9
    idx = -1
    for i in range(x, y+1):
        now = trip[i]
        if depth[now] < _min:
            _min = depth[now]
            idx = now
    return idx


dfs(1, 0)

for _ in range(int(input())):
    a, b = map(int, input().split())
    lca = find_lca(a, b)
    print(depth[a]+depth[b]-2*depth[lca])
