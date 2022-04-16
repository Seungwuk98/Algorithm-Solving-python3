import sys
input = sys.stdin.readline


def find(node):
    if node == parent[node]:
        return node
    parent[node] = find(parent[node])
    return parent[node]


def union(root1, root2):
    if rank[root1] > rank[root2]:
        parent[root2] = root1
    else:
        parent[root1] = root2
        if root1 == root2:
            rank[root2] += 1


n, m = map(int, input().split())
point = [[*map(int, input().split())]for _ in range(n)]
edges = []
for i in range(n-1):
    x1, y1 = point[i][0], point[i][1]
    for j in range(i+1, len(point)):
        x2, y2 = point[j][0], point[j][1]
        dist = ((x1-x2)**2+(y1-y2)**2)**0.5
        edges.append([dist, i, j])
edges.sort(reverse=True)
parent = [i for i in range(n)]
rank = [0]*n
distance = 0

for _ in range(m):
    i, j = map(int, input().split())
    root1, root2 = find(i-1), find(j-1)
    if root1 == root2:
        continue
    union(root1, root2)


while edges:
    dist, node1, node2 = edges.pop()
    root1 = find(node1)
    root2 = find(node2)

    if root1 == root2:
        continue
    union(root1, root2)
    distance += dist

print("%.2f" % distance)
