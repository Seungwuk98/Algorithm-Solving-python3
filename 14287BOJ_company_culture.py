import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

n, m = map(int, input().split())
arr = [*map(int, input().split())]
g = [[]for _ in range(n)]
for a, b in enumerate(arr):
    if b != -1:
        g[b-1].append(a)

pv = 0


def dfs(node=0):
    global pv
    iin[node] = pv
    pv += 1
    for next in g[node]:
        dfs(next)


iin = [0]*n
out = [0]*n
dfs()


class Node:
    def __init__(self, bottom, up) -> None:
        self.bottom = bottom
        self.up = up
        self.data = 0
        self.lazy = 0
        self.left = None
        self.right = None


class SegTree:
    def __init__(self) -> None:
        self.root = self.init(0, n-1)

    def init(self, bottom, up):
        node = Node(bottom, up)
        if bottom == up:
            return node
        mid = node.bottom + node.up >> 1
        node.left = self.init(bottom, mid)
        node.right = self.init(mid+1, up)
        return node

    def update(self, l, r, val):
        def do(node, l, r):
            if node.bottom == l and node.up == r:
                node.lazy += val
                self.prop(node)
                return

            self.prop(node)
            mid = (node.bottom + node.up) // 2
            if r <= mid:
                do(node.left, l, r)
                self.prop(node.right)
            elif l > mid:
                self.prop(node.left)
                do(node.right, l, r)
            else:
                do(node.left, l, mid)
                do(node.right, mid+1, r)
            node.data = node.left.data + node.right.data
        do(self.root, l, r)

    def find(self, i):
        def do(node):
            self.prop(node)
            if node.bottom == node.up:
                return node.data
            mid = node.bottom + node.up >> 1
            if i <= mid:
                return do(node.left)
            else:
                return do(node.right)
        return do(self.root)

    def prop(self, node):
        if not node.lazy:
            return
        c = node.up - node.bottom + 1
        node.data += node.lazy * c
        if node.left and node.right:
            node.left.lazy += node.lazy
            node.right.lazy += node.lazy
        node.lazy = 0


tree = SegTree()
for _ in range(m):
    qry = [*map(int, input().split())]
    qry[1] -= 1
    if qry[0] == 1:
        tree.update(iin[qry[1]], out[qry[1]], qry[2])
    else:
        print(tree.find(iin[qry[1]]))
