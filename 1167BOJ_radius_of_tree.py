import sys
from collections import deque
from itertools import combinations
input = sys.stdin.readline
sys.setrecursionlimit(100000)

n = int(input())
graph = [[]for _ in range(n+1)]
for _ in range(n):
    arr = [*map(int, input().split())]
    p = arr[0]
    for i in range(1, len(arr), 2):
        if arr[i] == -1:
            break
        graph[p].append((arr[i+1], arr[i]))

visit = [False]*(n+1)
visit[1] = True
radius = 0


def dfs(node, from_root):
    global radius
    r = []
    for next_dist, next_node in graph[node]:
        if visit[next_node]:
            continue
        visit[next_node] = True
        from_next_root = next_dist+from_root
        radius = max(radius, from_next_root)
        r.append(dfs(next_node, from_next_root))

    if len(r) >= 2:
        r.sort()
        radius = max(radius, r[-1]+r[-2]-from_root*2)
    if not r:
        return from_root
    return max(r)


dfs(1, 0)
print(radius)
