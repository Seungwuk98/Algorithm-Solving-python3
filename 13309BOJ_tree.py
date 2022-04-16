import sys
import os
import io
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
sys.setrecursionlimit(200020)

n, q = map(int, input().split())
g = [[]for _ in range(n+1)]
for i in range(2, n+1):
    a = int(input())
    g[a].append(i)

pv = 0
iin = [0]*(n+1)
out = [0]*(n+1)
dep = [0]*(n+1)
pr = [1]*n


def dfs(node=1):
    global pv
    iin[node] = pv
    pv += 1
    for next in g[node]:
        dep[next] = dep[node] + 1
        dfs(next)
    out[node] = pv-1


dfs()


class Node:
    def __init__(self, bottom, up) -> None:
        self.bottom = bottom
        self.up = up
        self.pr = 1
        self.lazy = 0
        self.right = None
        self.left = None


class SegTree:
    def __init__(self) -> None:
        self.root = self.init(0, n-1)

    def init(self, bottom, up):
        node = Node(bottom, up)
        if bottom == up:
            return node
        mid = bottom + up >> 1
        node.left = self.init(bottom, mid)
        node.right = self.init(mid+1, up)
        return node

    def prop(self, node):
        if not node.lazy or dep[node.pr] > dep[node.lazy]:
            node.lazy = 0
            return
        node.pr = node.lazy
        if node.left and node.right:
            node.left.lazy = node.lazy
            node.right.lazy = node.lazy
        node.lazy = 0

    def update(self, a, b, root):
        def do(node, a, b):
            if node.bottom == a and node.up == b:
                node.lazy = root
                self.prop(node)
                return

            self.prop(node)
            mid = node.bottom + node.up >> 1
            if b <= mid:
                self.prop(node.right)
                do(node.left, a, b)
            elif a > mid:
                do(node.right, a, b)
                self.prop(node.left)
            else:
                do(node.left, a, mid)
                do(node.right, mid+1, b)
        do(self.root, a, b)

    def find(self, x):
        def do(node):
            self.prop(node)
            if node.bottom == node.up:
                return node.pr
            mid = node.bottom + node.up >> 1
            if x <= mid:
                return do(node.left)
            else:
                return do(node.right)
        return do(self.root)


tree = SegTree()

for _ in range(q):
    b, c, d = map(int, input().split())
    rootb, rootc = tree.find(iin[b]), tree.find(iin[c])
    if d == 0:
        print('YES' if rootb == rootc else 'NO')
    else:
        if rootb == rootc:
            print('YES')
            tree.update(iin[b], out[b], b)
        else:
            print('NO')
            tree.update(iin[c], out[c], c)
