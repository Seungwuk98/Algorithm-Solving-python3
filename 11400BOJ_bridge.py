import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

v, e = map(int, input().split())
g = [[]for _ in range(v+1)]
for _ in range(e):
    a, b = map(int, input().split())
    g[a].append(b)
    g[b].append(a)


visit = [False] * (v+1)
depth = [0]*(v+1)
bridge = []
parent = [0]*(v+1)


def dfs(node, level):
    depth[node] = level
    ret = 10000001
    for next in g[node]:
        if not visit[next]:
            parent[next] = node
            visit[next] = True
            min_this = dfs(next, level+1)
            ret = min(ret, min_this)
            if min_this > level:
                x, y = node, next
                if x > y:
                    x, y = y, x
                bridge.append((x, y))
        elif next != parent[node]:
            ret = min(depth[next], ret)

    return ret


visit[1] = True
dfs(1, 0)
bridge.sort()
print(len(bridge))
for x in bridge:
    print(*x)
