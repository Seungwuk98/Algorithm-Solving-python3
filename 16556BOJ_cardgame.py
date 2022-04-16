from bisect import bisect_right
n, m, k = map(int, input().split())
cards = sorted([*map(int, input().split())])
parent = [*range(m)]
chul = [*map(int, input().split())]


def find(node):
    if parent[node] == node:
        return node
    parent[node] = find(parent[node])
    return parent[node]


for x in range(k):
    f = bisect_right(cards, chul[x])
    root = find(f)
    print(cards[root])
    parent[root] = root + 1
