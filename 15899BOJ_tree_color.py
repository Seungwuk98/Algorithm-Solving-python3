import sys
import os
import io
from bisect import bisect_right
sys.setrecursionlimit(200000)
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

n, m, c = map(int, input().split())
color = [*map(int, input().split())]
arr = [0]*n
iin = [0]*(n+1)
out = [0]*(n+1)
pv = 0
g = [[]for _ in range(n+1)]

for _ in range(n-1):
    a, b = map(int, input().split())
    g[a].append(b)
    g[b].append(a)

visit = [False] * (n+1)
visit[1] = True


def dfs(node=1):
    global pv
    iin[node] = pv
    arr[pv] = color[node-1]
    pv += 1
    for next in g[node]:
        if not visit[next]:
            visit[next] = True
            dfs(next)
    out[node] = pv-1


dfs()


def merge(ret, l, r):
    ll = len(l)
    rl = len(r)
    i = j = 0
    while True:
        if i == ll:
            while j < rl:
                ret.append(r[j])
                j += 1
            break
        elif j == rl:
            while i < ll:
                ret.append(l[i])
                i += 1
            break
        if l[i] < r[j]:
            ret.append(l[i])
            i += 1
        else:
            ret.append(r[j])
            j += 1
    return


class SegTree:
    def __init__(self) -> None:
        self.tree = [[]for _ in range(2*n)]
        for i in range(n):
            self.tree[i+n].append(arr[i])
        for i in range(n-1, 0, -1):
            merge(self.tree[i], self.tree[i << 1], self.tree[i << 1 | 1])

    def query(self, l, r, c):
        l += n
        r += n+1
        ret = 0
        while l < r:
            if l & 1:
                ret += bisect_right(self.tree[l], c)
                l += 1
            if r & 1:
                r -= 1
                ret += bisect_right(self.tree[r], c)
            l >>= 1
            r >>= 1
        return ret


tree = SegTree()

result = 0
for _ in range(m):
    a, b = map(int, input().split())
    result += tree.query(iin[a], out[a], b)
    result %= 1000000007
print(result)
