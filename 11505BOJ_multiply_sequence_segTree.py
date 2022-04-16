import sys
input = sys.stdin.readline
d = 1000000007


def pow(n, c):
    r = 1
    while n:
        if n & 1:
            r = r*c % d
        n >>= 1
        c = c*c % d
    return r


class Node:
    def __init__(self, bottom, up, mul, zeros) -> None:
        self.mul = mul
        self.bottom = bottom
        self.up = up
        self.mid = (bottom+up)//2
        self.zeros = zeros
        self.left = None
        self.right = None


class SegTree:
    def __init__(self, size, data) -> None:
        self.data = data
        r = 1
        zeros = 0
        self.zeros = [False]*(size+1)
        for i in range(size):
            x = data[i]
            if not x:
                self.zeros[i+1] = True
                zeros += 1
            r = (r*x) % d
        self.root = Node(1, size, r, zeros)
        self.root.left = self.make_tree(1, (1+size)//2)
        self.root.right = self.make_tree((1+size)//2+1, size)

    def make_tree(self, bottom, up):
        data = self.data[bottom-1:up]
        r = 1
        zeros = 0
        for i in range(len(data)):
            x = data[i]
            if not x:
                zeros += 1
            r = r*x % d
        node = Node(bottom, up, r, zeros)
        if bottom == up:
            return node
        mid = (bottom+up)//2
        node.left = self.make_tree(bottom, mid)
        node.right = self.make_tree(mid+1, up)
        return node

    def update(self, idx, new):
        tmp = self.data[idx-1]
        if self.zeros[idx] and new:
            self.zeros[idx] = False
            self.update_zeros(self.root, idx, -1)
        elif not self.zeros[idx] and not new:
            self.zeros[idx] = True
            self.update_zeros(self.root, idx, 1)
        if not tmp:
            if new:
                self.zeros[idx] = False
                self.data[idx-1] = new
                self.update_from_zero(self.root, idx, new)
        else:
            if new:
                self.data[idx-1] = new
                self.normal_update(self.root, idx, new, tmp)

    def update_zeros(self, node, idx, u_d):
        node.zeros += u_d
        if node.up == node.bottom:
            return
        if idx <= node.mid:
            self.update_zeros(node.left, idx, u_d)
        else:
            self.update_zeros(node.right, idx, u_d)

    def update_from_zero(self, node, idx, new):
        data = self.data[node.bottom-1:node.up]
        r = 1
        if node.zeros:
            for i in range(len(data)):
                x = data[i]
                r = r*x % d
            node.mul = r
        if node.up == node.bottom:
            return
        if idx <= node.mid:
            self.update_from_zero(node.left, idx, new)
        else:
            self.update_from_zero(node.right, idx, new)

    def normal_update(self, node, idx, new, old):
        node.mul = (node.mul*pow(d-2, old) % d)*new % d
        if node.up == node.bottom:
            return
        if idx <= node.mid:
            self.normal_update(node.left, idx, new, old)
        else:
            self.normal_update(node.right, idx, new, old)

    def query(self, node, bottom, up):
        if node.bottom == bottom and node.up == up:
            if node.zeros:
                return 0
            else:
                return node.mul
        left_mul, right_mul = 1, 1
        if up <= node.mid:
            left_mul = self.query(node.left, bottom, up)
        elif bottom > node.mid:
            right_mul = self.query(node.right, bottom, up)
        else:
            left_mul = self.query(node.left, bottom, node.mid)
            right_mul = self.query(node.right, node.mid+1, up)
        return left_mul * right_mul % d


n, m, k = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(int(input()))
tree = SegTree(n, arr)
for _ in range(m+k):
    a, b, c = map(int, input().split())
    if a == 1:
        tree.update(b, c)
    else:
        mul = tree.query(tree.root, b, c)
        print(mul)
