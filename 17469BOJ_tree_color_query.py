import sys
input = sys.stdin.readline
sys.setrecursionlimit(100500)
def minput(): return map(int, input().split())


n, q = minput()
tree = [*range(n+1)]
color = [0]*(n+1)
for i in range(n-1):
    tree[i+2] = int(input())
for i in range(n):
    color[i+1] = int(input())

qry = [[*minput()]for _ in range(n+q-1)]
qry.reverse()
result = []

parent = [*range(n+1)]
rank = [set([color[i]])for i in range(n+1)]


def find(node):
    if parent[node] == node:
        return node
    parent[node] = find(parent[node])
    return parent[node]


def union(node1, node2):
    root1, root2 = find(node1), find(node2)
    if root1 == root2:
        return False
    else:
        if len(rank[root1]) > len(rank[root2]):
            parent[root2] = root1
            rank[root1] |= rank[root2]
        else:
            parent[root1] = root2
            rank[root2] |= rank[root1]
    return True


for q in qry:
    a, b = q
    if a == 1:
        union(b, tree[b])
    else:
        result.append(len(rank[find(b)]))
result.reverse()
for x in result:
    print(x)
