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


def dfs(node, level, root):
    depth[node] = level
    child = 0
    ret = 1000000
    check = False
    for next in g[node]:
        if not visit[next]:
            child += 1
            visit[next] = True
            min_this = dfs(next, level+1, False)
            ret = min(ret, min_this)
            if min_this >= level:
                check = True
        else:
            ret = min(depth[next], ret)

    if root and child >= 2:
        bridge.append(node)
    elif not root and check:
        bridge.append(node)
    return ret


for i in range(1, v+1):
    if not visit[i]:
        visit[i] = True
        dfs(i, 0, True)
bridge.sort()
print(len(bridge))
print(*bridge)
