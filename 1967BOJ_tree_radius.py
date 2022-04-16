import sys
from itertools import combinations
sys.setrecursionlimit(100000)
input = sys.stdin.readline
n = int(input())

child = [[]for _ in range(n+1)]

for _ in range(n-1):
    a, b, c = map(int, input().split())
    child[a].append((c, b))

radius = 0


def dfs(node, dist):
    global radius
    if not child[node]:
        return dist
    r = []
    for next_dist, next_node in child[node]:
        r.append(dfs(next_node, next_dist))
    if len(r) >= 2:
        r_comb = combinations(r, 2)
        for x in r_comb:
            radius = max(radius, sum(x))
    else:
        radius = max(max(r)+dist, radius)
    return max(r) + dist


dfs(1, 0)
print(radius)
