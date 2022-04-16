import sys
input = sys.stdin.readline
n, m = map(int, input().split())
parent = [*range(n)]
rank = [0]*n


def find(node):
    if parent[node] == node:
        return node
    parent[node] = find(parent[node])
    return parent[node]


def union(node1, node2):
    root1, root2 = find(node1), find(node2)
    if root1 == root2:
        return False
    elif rank[root1] > rank[root2]:
        parent[root2] = root1
    else:
        parent[root1] = root2
        if rank[root1] == rank[root2]:
            rank[root2] += 1
    return True


c = False
for i in range(1, m+1):
    a, b = map(int, input().split())
    if not union(a, b):
        c = True
        break
if c:
    print(i)
else:
    print(0)
