import sys
input = sys.stdin.readline
n, m = map(int, input().split())
mat = [[*map(int, input().split())]for _ in range(n)]


class Node:
    def __init__(self, lo, hi) -> None:
        self.lo = lo
        self.hi = hi
        self.sum = 0
        self.left = self.right = None


class SegTree:
    def __init__(self, row) -> None:
        self.row = row-1
        self.root = self.init(1, n)

    def init(self, lo, hi):
        node = Node(lo, hi)
        if lo == hi:
            node.sum = mat[self.row][lo-1]
            return node
        mid = lo + hi >> 1
        node.left = self.init(lo, mid)
        node.right = self.init(mid+1, hi)
        node.sum = node.left.sum + node.right.sum
        return node

    def update(self, x, c):
        def do(node):
            if node.lo == node.hi:
                node.sum = c
                return
            mid = node.lo + node.hi >> 1
            do(node.left if x <= mid else node.right)
            node.sum = node.left.sum + node.right.sum
        do(self.root)

    def query(self, l, r):
        def do(node, l, r):
            if node.lo == l and node.hi == r:
                return node.sum
            mid = node.lo + node.hi >> 1
            if r <= mid:
                return do(node.left, l, r)
            elif l > mid:
                return do(node.right, l, r)
            else:
                return do(node.left, l, mid) + do(node.right, mid+1, r)
        return do(self.root, l, r)


class SegTree2D:
    def __init__(self) -> None:
        self.root = self.init(1, n)

    def init(self, lo, hi):
        node = Node(lo, hi)
        if lo == hi:
            node.sum = trees[lo-1]
            return node
        mid = lo + hi >> 1
        node.left = self.init(lo, mid)
        node.right = self.init(mid+1, hi)


trees = []
for i in range(1, n+1):
    trees.append(SegTree(i))
