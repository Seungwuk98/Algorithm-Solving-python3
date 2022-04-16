import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)
LOG = 18
n = int(input())
g = [[]for _ in range(n+1)]
arr = [*map(int, input().split())]

for _ in range(n-1):
    x, y = map(int, input().split())
    g[x].append(y)
    g[y].append(x)

iin = [0]*(n+1)
out = [0]*(n+1)
dep = [0]*(n+1)
tour = []
vst = [False]*(n+1)
vst[1] = True
pv = 0
parent = [[0]*LOG for _ in range(n+1)]


def dfs(node=1):
    global pv
    iin[node] = pv
    pv += 1
    tour.append(node)
    for next in g[node]:
        if not vst[next]:
            vst[next] = True
            parent[next][0] = node
            dep[next] = dep[node] + 1
            dfs(next)
    tour.append(node)
    out[node] = pv
    pv += 1


dfs()
for i in range(1, LOG):
    for j in range(1, n+1):
        parent[j][i] = parent[parent[j][i-1]][i-1]


def lca(a, b):
    if dep[a] < dep[b]:
        a, b = b, a
    for i in range(LOG-1, -1, -1):
        if dep[a] - dep[b] >= (1 << i):
            a = parent[a][i]
    if a == b:
        return a
    for i in range(LOG-1, -1, -1):
        if parent[a][i] != parent[b][i]:
            a = parent[a][i]
            b = parent[b][i]
    return parent[a][i]


nn = len(tour)
sn = int(nn**0.5)+1
m = int(input())
qry = []
for i in range(m):
    x, y = map(int, input().split())
    l = lca(x, y)
    if x == l or y == l:
        if y == l:
            x, y = y, x
        qry.append((iin[x], iin[y], i, -1))
    else:
        if out[x] < iin[y]:
            qry.append((out[x], iin[y], i, iin[l]))
        else:
            qry.append((out[y], iin[x], i, iin[l]))
qry.sort(key=lambda x: (x[0]//sn, x[1]))
buk1 = [0]*(n+1)
buk2 = [0]*1000001
now = 0


def insert(x):
    global now
    z = tour[x]
    y = arr[z-1]
    buk1[z] += 1
    if buk1[z] == 2:
        buk2[y] -= 1
        if not buk2[y]:
            now -= 1
    else:
        if not buk2[y]:
            now += 1
        buk2[y] += 1


def remove(x):
    global now
    z = tour[x]
    y = arr[z-1]
    if buk1[z] == 2:
        if not buk2[y]:
            now += 1
        buk2[y] += 1
    else:
        buk2[y] -= 1
        if not buk2[y]:
            now -= 1
    buk1[z] -= 1


li, lj, lk, ll = qry[0]
result = [0]*m
if ll != -1:
    insert(ll)
for x in range(li, lj+1):
    insert(x)
result[lk] = now
if ll != -1:
    remove(ll)

for w in range(1, m):
    ni, nj, nk, nl = qry[w]
    if nl != -1:
        insert(nl)
    if li//sn == ni//sn:
        for x in range(lj+1, nj+1):
            insert(x)
        if li < ni:
            for x in range(li, ni):
                remove(x)
        else:
            for x in range(ni, li):
                insert(x)
    else:
        if lj < nj:
            for x in range(lj+1, nj+1):
                insert(x)
        else:
            for x in range(nj+1, lj+1):
                remove(x)
        for x in range(li, ni):
            remove(x)
    result[nk] = now
    if nl != -1:
        remove(nl)
    li, lj, lk = ni, nj, nk

print('\n'.join(map(str, result)))
