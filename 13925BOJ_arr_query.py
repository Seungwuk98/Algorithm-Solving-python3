import sys
import os
import io
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

n = int(input())
arr = [*map(int, input().split())]
D = 1000000007


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
        self.root = self.init(1, n)

    def init(self, bottom, up):
        node = Node(bottom, up)
        if bottom == up:
            node.data = arr[up-1]
            return node
        mid = node.mid
        node.left = self.init(bottom, mid)
        node.right = self.init(mid+1, up)
        node.data = (node.left.data + node.right.data) % D
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


tree = SegTree()
for _ in range(int(input())):
    qry = [*map(int, input().split())]
    if qry[0] == 1:
        tree.update(qry[1], qry[2], qry[3], 1)
    elif qry[0] == 2:
        tree.update(qry[1], qry[2], 0, qry[3])
    elif qry[0] == 3:
        tree.update(qry[1], qry[2], qry[3], 0)
    else:
        print(tree.find(qry[1], qry[2]))
