import sys
import os
import io
sys.setrecursionlimit(500000)
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

n, q = map(int, input().split())
D = 1 << 32
g = [[]for _ in range(n)]
top = [0]*n
iin = [0]*n
out = [0]*n
sz = [1]*n
dep = [0]*n
par = [*range(n)]
for _ in range(n-1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    g[a].append(b)
    g[b].append(a)


def dfs1(node=0):
    msz = midx = 0
    for i in range(len(g[node])):
        next = g[node][i]
        if not visit[next]:
            visit[next] = True
            par[next] = node
            dep[next] = dep[node]+1
            dfs1(next)
            sz[node] += sz[next]
            if sz[next] > msz:
                msz = sz[next]
                midx = i
    if g[node]:
        g[node][0], g[node][midx] = g[node][midx], g[node][0]


pv = 0


def dfs2(node=0):
    global pv
    iin[node] = pv
    pv += 1
    for i in range(len(g[node])):
        next = g[node][i]
        if not visit[next]:
            visit[next] = True
            top[next] = next if i else top[node]
            dfs2(next)
    out[node] = pv-1


visit = [False]*n
visit[0] = True
dfs1()
visit = [False]*n
visit[0] = True
dfs2()


class Node:
    def __init__(self, bottom, up) -> None:
        self.data = 0
        self.bottom = bottom
        self.up = up
        self.mid = (bottom + up)//2
        self.left = None
        self.right = None
        self.lazy1 = 0
        self.lazy2 = 1


class SegTree:
    def __init__(self) -> None:
        self.root = self.init(0, n-1)

    def init(self, bottom, up):
        node = Node(bottom, up)
        if bottom == up:
            return node
        mid = node.mid
        node.left = self.init(bottom, mid)
        node.right = self.init(mid+1, up)
        return node

    def update(self, l, r, pl, mul):
        if l > r:
            l, r = r, l

        def do(node, l, r):
            self.prop(node)
            if node.bottom == l and node.up == r:
                node.lazy1 = (node.lazy1 + pl) % D
                node.lazy2 = (node.lazy2 * mul) % D
                self.prop(node)
                return

            mid = node.mid
            if r <= mid:
                self.prop(node.right)
                do(node.left, l, r)
            elif l > mid:
                self.prop(node.left)
                do(node.right, l, r)
            else:
                do(node.left, l, mid)
                do(node.right, mid+1, r)
            node.data = (node.left.data + node.right.data) % D
        do(self.root, l, r)

    def prop(self, node):
        if node.lazy1 == 0 and node.lazy2 == 1:
            return
        c = node.up - node.bottom + 1
        node.data = (node.lazy2*node.data % D + node.lazy1*c % D) % D
        if node.left:
            node.left.lazy1 *= node.lazy2
            node.left.lazy1 %= D
            node.left.lazy1 += node.lazy1
            node.left.lazy1 %= D
            node.left.lazy2 *= node.lazy2
            node.left.lazy2 %= D
        if node.right:
            node.right.lazy1 *= node.lazy2
            node.right.lazy1 %= D
            node.right.lazy1 += node.lazy1
            node.right.lazy1 %= D
            node.right.lazy2 *= node.lazy2
            node.right.lazy2 %= D
        node.lazy1 = 0
        node.lazy2 = 1

    def find(self, l, r):
        if l > r:
            l, r = r, l

        def do(node, l, r):
            self.prop(node)
            if node.bottom == l and node.up == r:
                return node.data

            if r <= node.mid:
                self.prop(node.right)
                return do(node.left, l, r)
            elif l > node.mid:
                self.prop(node.left)
                return do(node.right, l, r)
            else:
                return (do(node.left, l, node.mid) +
                        do(node.right, node.mid+1, r)) % D
        return do(self.root, l, r)


def query_sum(a, b):
    ret = 0
    while top[a] != top[b]:
        if dep[top[a]] < dep[top[b]]:
            a, b = b, a
        st = top[a]
        ret = (ret + tree.find(iin[st], iin[a])) % D
        a = par[st]
    if dep[a] > dep[b]:
        a, b = b, a
    ret = (ret + tree.find(iin[a], iin[b])) % D
    return ret


def query_update(a, b, pl, mul):
    while top[a] != top[b]:
        if dep[top[a]] < dep[top[b]]:
            a, b = b, a
        st = top[a]
        tree.update(iin[st], iin[a], pl, mul)
        a = par[st]
    if dep[a] > dep[b]:
        a, b = b, a
    tree.update(iin[a], iin[b], pl, mul)


tree = SegTree()

for _ in range(q):
    qry = [*map(int, input().split())]
    a = qry[1]-1
    if qry[0] == 1:
        b = qry[2]
        tree.update(iin[a], out[a], b, 1)
    elif qry[0] == 2:
        b = qry[2]-1
        c = qry[3]
        query_update(a, b, c, 1)
    elif qry[0] == 3:
        b = qry[2]
        tree.update(iin[a], out[a], 0, b)
    elif qry[0] == 4:
        b = qry[2]-1
        c = qry[3]
        query_update(a, b, 0, c)
    elif qry[0] == 5:
        sys.stdout.write('{}\n'.format(tree.find(iin[a], out[a])))
    else:
        b = qry[2]-1
        sys.stdout.write('{}\n'.format(query_sum(a, b)))
