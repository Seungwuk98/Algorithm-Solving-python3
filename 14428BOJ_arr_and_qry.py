import sys
input = sys.stdin.readline


class Node:
    def __init__(self, bottom, up, min_value, min_idx) -> None:
        self.min_value = min_value
        self.up = up
        self.bottom = bottom
        self.mid = (up+bottom)//2
        self.min_idx = min_idx
        self.left = None
        self.right = None


class SegTree:
    def __init__(self, size, data):
        self.data = data
        self.size = size
        _min = min(data)
        mid = (1+size)//2
        self.root = Node(1, size, _min, data.index(_min)+1)
        self.root.left = self.make_tree(1, mid)
        self.root.right = self.make_tree(mid+1, size)

    def make_tree(self, bottom, up):
        data = self.data[bottom-1:up]
        mid = (bottom+up)//2
        _min = min(data)
        node = Node(bottom, up, _min, data.index(_min)+bottom)
        if bottom == up:
            return node
        node.left = self.make_tree(bottom, mid)
        node.right = self.make_tree(mid+1, up)
        return node

    def update(self, node, idx, v):
        if node.min_value == v:
            node.min_idx = min(node.min_idx, idx)
        elif node.min_value > v:
            node.min_value = v
            node.min_idx = idx
        elif node.min_idx == idx:
            data = self.data[node.bottom-1:node.up]
            node.min_value = min(data)
            node.min_idx = data.index(node.min_value)+node.bottom

        if node.up == node.bottom:
            return
        if node.mid >= idx:
            self.update(node.left, idx, v)
        else:
            self.update(node.right, idx, v)

    def find_min_idx(self, node, bottom, up):
        if node.up == up and node.bottom == bottom:
            return node.min_value, node.min_idx
        left_min, left_idx = 1e10, -1
        right_min, right_idx = 1e10, -1
        if up <= node.mid:
            left_min, left_idx = self.find_min_idx(node.left, bottom, up)
        elif bottom > node.mid:
            right_min, right_idx = self.find_min_idx(node.right, bottom, up)
        else:
            left_min, left_idx = self.find_min_idx(node.left, bottom, node.mid)
            right_min, right_idx = self.find_min_idx(
                node.right, node.mid+1, up)
        if left_min <= right_min:
            return left_min, left_idx
        else:
            return right_min, right_idx


n = int(input())
arr = [*map(int, input().split())]
tree = SegTree(n, arr)
for _ in range(int(input())):
    a, b, c = map(int, input().split())
    if a == 1:
        tree.data[b-1] = c
        tree.update(tree.root, b, c)
    else:
        min_value, min_idx = tree.find_min_idx(tree.root, b, c)
        print(min_idx)
