import copy


def union(node1, node2):
    if rank[node1] > rank[node2]:
        parent[node2] = node1
    else:
        parent[node1] = node2
        if rank[node1] == rank[node2]:
            rank[node2] += 1


def krus(tmp, weight, start_node, end_node):
    while tmp:
        visit = tmp.pop()
        if visit[0] < weight:
            continue
        node1, node2 = find(visit[1]), find(visit[2])
        if node1 != node2:
            union(node1, node2)
        if find(start_node) == find(end_node):
            return True
    return False


def find(node):
    if parent[node] == node:
        return node
    else:
        parent[node] = find(parent[node])
    return parent[node]


n, m = map(int, input().split())

bridges = list()
min, max = 1000000000, 1
for _ in range(m):
    k1, k2, bridge = map(int, input().split())
    if min > bridge:
        min = bridge
    if max < bridge:
        max = bridge
    bridges.append((bridge, k1, k2))

start, end = map(int, input().split())

available = 0

while min <= max:
    weight = (min + max)//2
    parent = {i: i for i in range(1, n + 1)}
    rank = {i: 0 for i in range(1, n + 1)}
    tmp = copy.deepcopy(bridges)
    if krus(tmp, weight, start, end):
        min = weight+1
        available = weight
    else:
        max = weight-1

print(available)
