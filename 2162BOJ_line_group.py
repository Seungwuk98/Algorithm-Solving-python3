n = int(input())

line = [[*map(int, input().split())]for _ in range(n)]
parent = [i for i in range(n)]
rank = [1]*n


def find(idx):
    if parent[idx] == idx:
        return idx
    parent[idx] = find(parent[idx])
    return parent[idx]


def union(idx1, idx2):
    root1, root2 = find(idx1), find(idx2)
    if root1 == root2:
        return False
    elif rank[root1] > rank[root2]:
        parent[root2] = root1
        rank[root1] += rank[root2]
    else:
        parent[root1] = root2
        rank[root2] += rank[root1]
    return True


def check(line1, line2):
    x1, y1, x2, y2 = line1
    x3, y3, x4, y4 = line2
    c1 = ccw(x1, y1, x2, y2, x3, y3)*ccw(x1, y1, x2, y2, x4, y4)
    c2 = ccw(x3, y3, x4, y4, x1, y1)*ccw(x3, y3, x4, y4, x2, y2)
    if c1 <= 0 and c2 <= 0:
        if c1 == 0 and c2 == 0:
            if min(x1, x2) <= max(x3, x4) and min(x3, x4) <= max(x1, x2) and min(y1, y2) <= max(y3, y4) and min(y3, y4) <= max(y1, y2):
                return True
            else:
                return False
        else:
            return True
    else:
        return False


def ccw(x1, y1, x2, y2, x3, y3):
    return (x2-x1)*(y3-y1)-(y2-y1)*(x3-x1)


for i in range(n-1):
    for j in range(i+1, n):
        if check(line[i], line[j]):
            union(i, j)
for i in range(n):
    find(i)
print(len(set(parent)))
print(max(rank))
