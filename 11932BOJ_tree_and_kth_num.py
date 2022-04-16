import sys
from bisect import *
input = sys.stdin.readline
n, m = map(int, input().split())
arr = [*map(int, input().split())]
g = [[]for _ in range(n+1)]
for _ in range(n-1):
    x, y = map(int, input().split())
    g[x].append(y)
    g[y].append(x)

iin = [0]*(n+1)
top = [*range(n+1)]
dep = [0]*(n+1)
par = [*range(n+1)]
sz = [1]*(n+1)
narr = [0]*n
vst = [False]*(n+1)


def dfs1(node=1):
    msz, midx = 0, -1
    for i in range(len(g[node])):
        next = g[node][i]
        if not vst[next]:
            vst[next] = True
            dep[next] = dep[node] + 1
            par[next] = node
            dfs1(next)
            sz[node] += sz[next]
            if sz[next] > msz:
                msz = sz[next]
                midx = i
    if g[node]:
        g[node][0], g[node][midx] = g[node][midx], g[node][0]


pv = 0


def dfs2(node=1):
    global pv
    iin[node] = pv
    narr[pv] = arr[node-1]
    pv += 1
    for i in range(len(g[node])):
        next = g[node][i]
        if not vst[next]:
            vst[next] = True
            top[next] = next if i else top[node]
            dfs2(next)


vst[1] = True
dfs1()
vst = [False]*(n+1)
vst[1] = True
dfs2()

bit = [[]for _ in range(n+1)]
for i in range(1, n+1):
    bit[i] = sorted(narr[i-(i & -i):i])
narr.sort()


def find(l, r, x):
    under = below = 0
    r += 1
    while r:
        under += bisect_left(bit[r], x)
        below += bisect_right(bit[r], x)
        r -= r & -r
    while l:
        under -= bisect_left(bit[l], x)
        below -= bisect_right(bit[l], x)
        l -= l & -l
    return under, below


def find2(a, b, x):
    under = below = 0
    while top[a] != top[b]:
        if dep[top[a]] < dep[top[b]]:
            a, b = b, a
        st = top[a]
        r, w = find(iin[st], iin[a], x)
        under += r
        below += w
        a = par[st]
    if dep[a] > dep[b]:
        a, b = b, a
    r, w = find(iin[a], iin[b], x)
    return under+r, below+w


def bi(a, b, k):
    lo, hi = 0, n
    while lo < hi:
        mid = lo+hi >> 1
        under, below = find2(a, b, narr[mid])
        if below < k:
            lo = mid+1
        elif under >= k:
            hi = mid-1
        else:
            return narr[mid]
    return narr[lo]


for _ in range(m):
    a, b, k = map(int, input().split())
    print(bi(a, b, k))
