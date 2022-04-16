import sys
input = sys.stdin.readline

n = int(input())
dep = [0]*(n+1)
sz = [1]*(n+1)
top = [1]*(n+1)
pr = [0]*(n+1)
iin = [0]*(n+1)
arr = [*map(int, input().split())]
narr = [0]*n
vst = [False]*(n+1)
g = [[]for _ in range(n+1)]

for _ in range(n-1):
    x, y = map(int, input().split())
    g[x].append(y)
    g[y].append(x)


def dfs1(node=1):
    midx = msz = 0
    for i in range(len(g[node])):
        nxt = g[node][i]
        if not vst[nxt]:
            vst[nxt] = True
            dep[nxt] = dep[node]+1
            pr[nxt] = node
            dfs1(nxt)
            sz[node] += sz[nxt]
            if sz[nxt] > msz:
                msz = sz[nxt]
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
        nxt = g[node][i]
        if not vst[nxt]:
            vst[nxt] = True
            top[nxt] = nxt if i else top[node]
            dfs2(nxt)


vst[1] = 1
dfs1()
vst = [0]*(n+1)
vst[1] = 1
dfs2()


class Node:
    def __init__(self) -> None:
        self.lmax = self.rmax = self.max = self.sum = 0
        self.lazy = -20000
        self.left = self.right = None


def merge(a, b):
    ret = Node()
    ret.sum = a.sum + b.sum
    ret.lmax = max(a.lmax, a.sum + b.lmax)
    ret.rmax = max(b.rmax, a.rmax + b.sum)
    ret.max = max(a.max, b.max, a.rmax + b.lmax)
    ret.left = a
    ret.right = b
    return ret


class Segtree:
    def __init__(self) -> None:
        self.tree = self.init(0, n-1)

    def init(self, lo, hi):
        if lo == hi:
            node = Node()
            node.lmax = node.rmax = node.max = node.sum = narr[lo]
            return node
        mid = lo + hi >> 1
        left = self.init(lo, mid)
        right = self.init(mid+1, hi)
        node = merge(left, right)
        return node

    def prop(self, node, lo, hi):
        if node.lazy == -20000:
            return
        node.sum = (hi-lo+1)*node.lazy
        if node.lazy <= 0:
            node.lmax = node.rmax = node.max = 0
        else:
            node.lmax = node.rmax = node.max = node.sum
        if lo != hi:
            node.left.lazy = node.right.lazy = node.lazy
        node.lazy = -20000

    def update(self, node, lo, hi, s, e, w):
        self.prop(node, lo, hi)
        if hi < s or e < lo:
            return
        if s <= lo and hi <= e:
            node.lazy = w
            self.prop(node, lo, hi)
            return
        mid = lo + hi >> 1
        self.update(node.left, lo, mid, s, e, w)
        self.update(node.right, mid+1, hi, s, e, w)

    def query(self, node, lo, hi, s, e):
        self.prop(node, lo, hi)
        if hi < s or e < lo:
            return Node()
        if s <= lo and hi <= e:
            return node
        mid = lo + hi >> 1
        return merge(self.query(node.left, lo, mid, s, e), self.query(node.right, mid+1, hi, s, e))


tree = Segtree()


def lca(u, v):
    while top[u] != top[v]:
        if dep[top[u]] < dep[top[v]]:
            u, v = v, u
        u = pr[top[u]]
    if dep[u] > dep[v]:
        u, v = v, u
    return u


def query_update(u, v, w):
    while top[u] != top[v]:
        if dep[top[u]] < dep[top[v]]:
            u, v = v, u
        st = top[u]
        tree.update(tree.tree, 0, n-1, iin[st], iin[u], w)
        u = pr[st]
    if dep[u] > dep[v]:
        u, v = v, u
    tree.update(tree.tree, 0, n-1, iin[u], iin[v], w)


def query_ans(u, v):
    l = lca(u, v)
    left, right = Node(), Node()
    while top[u] != top[l]:
        st = top[u]
        tmp = tree.query(tree.tree, 0, n-1, iin[st], iin[u])
        tmp.lmax, tmp.rmax = tmp.rmax, tmp.lmax
        left = merge(left, tmp)
        u = pr[st]
    while top[v] != top[l]:
        st = top[v]
        tmp = tree.query(tree.tree, 0, n-1, iin[st], iin[v])
        right = merge(tmp, right)
        v = pr[st]
    if dep[u] < dep[v]:
        tmp = tree.query(tree.tree, 0, n-1, iin[u], iin[v])
    else:
        tmp = tree.query(tree.tree, 0, n-1, iin[v], iin[u])
    left = merge(left, tmp)
    left = merge(left, right)
    return left.max


for _ in range(int(input())):
    q = [*map(int, input().split())]
    if q[0] == 1:
        print(query_ans(q[1], q[2]))
    else:
        query_update(q[1], q[2], q[3])
