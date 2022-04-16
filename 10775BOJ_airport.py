g = int(input())
p = int(input())
parent = [*range(g+1)]
left_max = [*range(g+1)]
docked = [False]*(g+2)


def find(node):
    if parent[node] == node:
        return node
    parent[node] = find(parent[node])
    left_max[parent[node]] = min(left_max[node], left_max[parent[node]])
    return parent[node]


r = 0
for _ in range(p):
    x = int(input())
    if docked[x]:
        x = left_max[find(x)]
    if not x:
        break
    r += 1
    docked[x] = True
    if docked[x-1] and docked[x+1]:
        parent[x-1] = x
        parent[x] = x+1
        find(x-1)
    elif docked[x-1]:
        parent[x-1] = x
        left_max[x] = left_max[x-1]
    elif docked[x+1]:
        parent[x] = x+1
        left_max[x] = x-1
        find(x)
    else:
        left_max[x] = x-1
print(r)
