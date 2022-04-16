from heapq import *
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
edge = []
parent = [i for i in range(n+1)]
rank = [0 for _ in range(n+1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    edge.append((c, a, b))
edge.sort()


def find(node):
    if parent[node] == node:
        return node
    parent[node] = find(parent[node])
    return parent[node]


def union(node1, node2):
    root1, root2 = find(node1), find(node2)
    if root1 == root2:
        return False
    if rank[root1] > rank[root2]:
        parent[root2] = root1
    else:
        parent[root1] = root2
        if rank[root1] == rank[root2]:
            rank[root2] += 1
    return True


def kruskal(egde):
    r = 0
    max_edge = 0
    for c, a, b in edge:

        if union(a, b):
            r += c
            max_edge = max(max_edge, c)
    return max_edge, r


max_edge, r = kruskal(edge)
print(r-max_edge)
