cases = int(input())
result = []


def make_set(node):
    parent[node] = node
    rank[node] = 0
    society[node] = 1


def find(node):
    if parent[node] != node:
        parent[node] = find(parent[node])
    return parent[node]


def union(node1, node2):
    root1 = find(node1)
    root2 = find(node2)
    if root1 == root2:
        return
    if rank[root1] > rank[root2]:
        parent[root2] = root1
        society[root1] += society[root2]
    elif rank[root1] > rank[root2]:
        parent[root1] = root2
        society[root2] += society[root1]
    else:
        parent[root2] = root1
        rank[root1] += 1
        society[root1] += society[root2]


for _ in range(cases):
    roots = []
    parent = dict()
    rank = dict()
    society = dict()
    friend_rel_num = int(input())
    for i in range(friend_rel_num):
        a, b = list(input().split(' '))
        if a not in parent.keys():
            make_set(a)
        if b not in parent.keys():
            make_set(b)
        union(a, b)
        result.append(society[find(a)])

for i in range(len(result)):
    print(result[i])
