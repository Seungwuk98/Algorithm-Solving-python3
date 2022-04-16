import sys
import os
import io
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
sys.setrecursionlimit(100010)
INF = int(1e9)
n = int(input())
iin = [0]*n
ori = [0]*n
parent = [0]*n
size = [1]*n
top = [0]*n
depth = [0]*n
arr = [0]*n
g = [[]for _ in range(n)]
for _ in range(n-1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    g[a].append(b)
    g[b].append(a)


def dfs1(node=0):
    msz = 0
    midx = 0
    for i in range(len(g[node])):
        next = g[node][i]
        if not visit[next]:
            visit[next] = True
            depth[next] = depth[node]+1
            parent[next] = node
            dfs1(next)
            size[node] += size[next]
            if msz < size[next]:
                msz = size[next]
                midx = i
    if g[node]:
        g[node][0], g[node][midx] = g[node][midx], g[node][0]


pv = 0


def dfs2(node=0):
    global pv
    iin[node] = pv
    ori[pv] = node
    pv += 1
    for i in range((len(g[node]))):
        next = g[node][i]
        if not visit[next]:
            visit[next] = True
            top[next] = next if i else top[node]
            dfs2(next)


visit = [False]*n
visit[0] = True
dfs1()
visit = [False]*n
visit[0] = True
dfs2()


class SegTree:
    def __init__(self) -> None:
        self.tree = [INF]*(2*n)

    def update(self, i):
        self.tree[i+n] = INF if self.tree[i+n] == i else i
        i += n
        while i > 1:
            self.tree[i >> 1] = min(self.tree[i], self.tree[i ^ 1])
            i >>= 1

    def query(self, l, r):
        l += n
        r += n+1
        ret = INF
        while l < r:
            if l & 1:
                ret = min(ret, self.tree[l])
                l += 1
            if r & 1:
                r -= 1
                ret = min(ret, self.tree[r])
            l >>= 1
            r >>= 1
        return ret


def query(a):
    ret = INF
    while top[a]:
        st = top[a]
        ret = min(ret, tree.query(iin[st], iin[a]))
        a = parent[st]
    ret = min(ret, tree.query(0, iin[a]))
    if ret == INF:
        return -1
    return ori[ret]+1


tree = SegTree()
result = []
for _ in range(int(input())):
    q, a = map(int, input().split())
    a -= 1
    if q == 1:
        tree.update(iin[a])
    else:
        result.append(str(query(a)))

sys.stdout.write('\n'.join(result))
