import sys
input = sys.stdin.readline


class Node:
    def __init__(self, bottom, up) -> None:
        self.data = 0
        self.bottom = bottom
        self.up = up
        self.mid = (bottom+up)//2
        self.left = None
        self.right = None


class SegTree:
    def __init__(self) -> None:
        self.data = [0]*(1000001)
        self.root = self.init(1, 1000000)

    def init(self, bottom, up):
        node = Node(bottom, up)
        if bottom == up:
            return node
        mid = (bottom+up)//2
        node.left = self.init(bottom, mid)
        node.right = self.init(mid+1, up)
        return node

    def update_ord(self, taste, num):
        self.data[taste] += num
        self.update(self.root, taste, num)

    def update(self, node, taste, num):
        node.data += num
        if node.bottom == node.up:
            return

        if taste <= node.mid:
            self.update(node.left, taste, num)
        else:
            self.update(node.right, taste, num)

    def find_ord(self, k):
        taste = self.find(self.root, k, 0)
        self.update_ord(taste, -1)
        return taste

    def find(self, node, k, now):
        if node.bottom == node.up:
            return node.up

        if now + node.left.data < k:
            return self.find(node.right, k, now+node.left.data)
        else:
            return self.find(node.left, k, now)


tree = SegTree()
for _ in range(int(input())):
    qry = [*map(int, input().split())]
    if qry[0] == 1:
        print(tree.find_ord(qry[1]))
    else:
        tree.update_ord(qry[1], qry[2])
