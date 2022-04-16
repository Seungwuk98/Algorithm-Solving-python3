import sys
sys.setrecursionlimit(50000)

n, m = map(int, input().split())
s, e = map(int, input().split())
edge = []
for _ in range(m):
    x, y, w = map(int, input().split())
    edge.append((w, x, y))

edge.sort(reverse=True)
parent = [*range(n+1)]
rank = [0]*(n+1)


def find(node):
    if parent[node] == node:
        return node
    parent[node] = find(parent[node])
    return parent[node]


def union(node1, node2):
    root1, root2 = find(node1), find(node2)
    if root1 == root2:
        return
    if rank[root1] < rank[root2]:
        parent[root1] = root2
    else:
        parent[root2] = root1
        if rank[root1] == rank[root2]:
            rank[root1] += 1


edge.sort(reverse=True)
result = 0
for w, x, y in edge:
    union(x, y)
    if find(s) == find(e):
        result = w
        break

if find(s) == find(e):
    print(result)
else:
    print(0)
