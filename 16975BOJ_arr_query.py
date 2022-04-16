import sys
input = sys.stdin.readline
n = int(input())
arr = [*map(int, input().split())]


class Node:
    def __init__(self, bottom, up) -> None:
        self.bottom = bottom
        self.up = up
        self.mid = (bottom+up)//2
        self.left = None
        self.right = None
        self.lazy = 0


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

    def update_ord(self, i, j, k):
        i -= 1
        j -= 1
        if i > j:
            i, j = j, i
        self.update(self.root, i, j, k)

    def update(self, node, i, j, k):
        if node.bottom == i and node.up == j:
            node.lazy += k
            return

        if j <= node.mid:
            self.update(node.left, i, j, k)
        elif i > node.mid:
            self.update(node.right, i, j, k)
        else:
            self.update(node.left, i, node.mid, k)
            self.update(node.right, node.mid+1, j, k)

    def query(self, x):
        x -= 1
        return self.find(self.root, x)

    def find(self, node, x):
        if node.lazy:
            for i in range(node.bottom, node.up+1):
                arr[i] += node.lazy
            node.lazy = 0

        if node.bottom == node.up:
            return arr[x]

        if x <= node.mid:
            return self.find(node.left, x)
        else:
            return self.find(node.right, x)


tree = SegTree()
for _ in range(int(input())):
    qry = [*map(int, input().split())]
    if qry[0] == 1:
        tree.update_ord(qry[1], qry[2], qry[3])
    else:
        print(tree.query(qry[1]))
