n, m = map(int, input().split())
truth = [*map(int, input().split())][1:]
parent = [i for i in range(n+1)]
rank = [0 for i in range(n+1)]


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


for i in truth:
    for j in truth:
        union(i, j)
parties = []
for _ in range(m):
    r = [*map(int, input().split())]
    for i in r[1:]:
        for j in r[1:]:
            if i in truth:
                union(j, i)
            else:
                union(i, j)
    parties.append(r[1:])
if truth:
    truth.append(find(truth[0]))


result = 0
for party in parties:
    for people in party:
        root = find(people)
        if root in truth:
            break
    else:
        result += 1
print(result)
