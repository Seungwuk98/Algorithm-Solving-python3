import sys
input = sys.stdin.readline


n, q = map(int, input().split())
tree = [i for i in range(n+1)]
for i in range(1, n):
    tree[i+1] = int(input())

parent = [i for i in range(n+1)]
rank = [0]*(n+1)
querys = [[*map(int, input().split())]for _ in range(n-1+q)]
querys.reverse()


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


r = []
for query in querys:
    if query[0] == 0:
        union(query[1], tree[query[1]])
    else:
        root1, root2 = find(query[1]), find(query[2])
        if root1 != root2:
            r.append('NO')
        else:
            r.append('YES')
r.reverse()
print("\n".join(r))
