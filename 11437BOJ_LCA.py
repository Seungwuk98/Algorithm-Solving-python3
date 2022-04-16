import sys
from collections import deque
input = sys.stdin.readline
n = int(input())

tree = [[]for _ in range(n+1)]
for _ in range(n-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

depth = [0]*(n+1)
visit = [False]*(n+1)
visit[1] = True
parent = [0]*(n+1)
parent[1] = 1
s = deque([(1, 0)])
while s:
    node, level = s.popleft()
    depth[node] = level
    for next in tree[node]:
        if not visit[next]:
            visit[next] = True
            parent[next] = node
            s.append((next, level+1))

mem = {}
for _ in range(int(input())):
    a, b = map(int, input().split())
    if depth[a] > depth[b]:
        a, b = b, a
    t = (a, b)
    if t in mem:
        print(mem[t])
        continue
    while depth[b] != depth[a]:
        b = parent[b]
    while a != b:
        b = parent[b]
        a = parent[a]
    mem[t] = a
    print(a)
