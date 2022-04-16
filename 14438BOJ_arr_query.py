class Node:
    def __init__(self, data, bottom, up) -> None:
        self.data = data
        self.bottom = bottom
        self.up = up
        self.mid = (bottom+up)//2


class SegTree:
    def __init__(self) -> None:
        self.root = self.init(0, n-1)

    def init(self, bottom, up):
        node = Node(None, bottom, up)
        if bottom == up:
            node.data = arr[up]
            return node
        mid = node.mid
        node.left = self.init(bottom, mid)
        node.right = self.init(mid+1, up)
        node.data = min(node.left.data, node.right.data)
        return node

    def update_ord(self, i, v):
        i -= 1
        self.update(self.root, i, v)

    def update(self, node, i, v):
        if node.bottom == node.up:
            node.data = v
            return v

        if i <= node.mid:
            x = self.update(node.left, i, v)
            y = node.right.data
        else:
            x = self.update(node.right, i, v)
            y = node.left.data
        node.data = min(x, y)
        return node.data

    def find_ord(self, i, j):
        i -= 1
        j -= 1
        return self.find(self.root, i, j)

    def find(self, node, i, j):
        if node.bottom == i and node.up == j:
            return node.data

        left, right = [int(1e9)]*2
        if j <= node.mid:
            left = self.find(node.left, i, j)
        elif i > node.mid:
            right = self.find(node.right, i, j)
        else:
            left = self.find(node.left, i, node.mid)
            right = self.find(node.right, node.mid+1, j)
        return min(left, right)


n = int(input())
arr = [*map(int, input().split())]
tree = SegTree()

for _ in range(int(input())):
    a, b, c = map(int, input().split())
    if a == 1:
        tree.update_ord(b, c)
    else:
        print(tree.find_ord(b, c))
