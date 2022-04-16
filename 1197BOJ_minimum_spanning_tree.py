from heapq import *
import sys
input = sys.stdin.readline
v, e = map(int, input().split())
edge = []
for _ in range(e):
    a, b, c = map(int, input().split())
    heappush(edge, (c, a, b))
parent = [i for i in range(0, v+1)]
rank = [0]*(v+1)


def find(node):
    if parent[node] == node:
        return node
    parent[node] = find(parent[node])
    return parent[node]


def union(node1, node2):
    root1 = find(node1)
    root2 = find(node2)
    if root1 == root2:
        return False
    elif rank[root1] > rank[root2]:
        parent[root2] = root1
    else:
        parent[root1] = root2
        if rank[root1] == rank[root2]:
            rank[root2] += 1
    return True


def kruskal():
    r = 0
    while edge:
        dist, node1, node2 = heappop(edge)
        if union(node1, node2):
            r += dist
    return r


print(kruskal())
