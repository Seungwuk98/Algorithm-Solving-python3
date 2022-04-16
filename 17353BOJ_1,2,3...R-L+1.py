import os
import io
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

n = int(input())
arr = [*map(int, input().split())]


class Node:
    def __init__(self, bottom, up) -> None:
        self.lazyL = 0
        self.visit = 0
        self.bottom = bottom
        self.up = up
        self.mid = (bottom+up)//2
        self.left = None
        self.right = None


class SegTree:
    def __init__(self) -> None:
        self.root = self.init(0, n-1)

    def init(self, bottom, up):
        if bottom == up:
            return Node(bottom, up)

        node = Node(bottom, up)
        mid = node.mid
        node.left = self.init(bottom, mid)
        node.right = self.init(mid+1, up)
        return node

    def insert_ord(self, l, r):
        l -= 1
        r -= 1
        self.insert(self.root, l, r, 1)

    def insert(self, node, l, r, lv):
        if node.bottom == l and node.up == r:
            node.lazyL += lv
            node.visit += 1
            return

        if r <= node.mid:
            self.insert(node.left, l, r, lv)
        elif l > node.mid:
            self.insert(node.right, l, r, lv)
        else:
            self.insert(node.left, l, node.mid, lv)
            self.insert(node.right, node.mid+1, r, lv+node.mid-l+1)

    def find_ord(self, x):
        x -= 1
        return self.find(self.root, x)

    def find(self, node, x):
        if node.lazyL:
            self.propa(node)

        if node.bottom == node.up:
            return arr[node.up]

        if x <= node.mid:
            return self.find(node.left, x)
        else:
            return self.find(node.right, x)

    def propa(self, node):
        p = node.lazyL
        v = node.visit
        i = node.bottom
        while i <= node.up:
            arr[i] += p
            p += v
            i += 1
        node.lazyL = 0
        node.visit = 0


tree = SegTree()
for _ in range(int(input())):
    qry = [*map(int, input().split())]
    if qry[0] == 1:
        tree.insert_ord(qry[1], qry[2])
    else:
        print(tree.find_ord(qry[1]))
