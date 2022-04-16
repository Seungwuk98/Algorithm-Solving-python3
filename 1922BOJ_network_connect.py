n = int(input())
m = int(input())
edge = []
for _ in range(m):
    a, b, c = map(int, input().split())
    edge.append((c, a, b))

edge.sort()
parent = [i for i in range(n+1)]
rank = [0]*(n+1)


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


r = 0
for c, a, b in edge:
    if union(a, b):
        r += c
print(r)
