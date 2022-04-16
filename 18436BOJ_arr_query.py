import sys
input = sys.stdin.readline

n = int(input())
arr = [*map(int, input().split())]


class SegTree:
    def __init__(self) -> None:
        self.tree = [[0]*2 for _ in range(2*n)]
        for i in range(n):
            self.tree[i+n][arr[i] % 2] = 1
        for i in range(n-1, 0, -1):
            self.tree[i][0] = self.tree[i << 1][0] + self.tree[i << 1 | 1][0]
            self.tree[i][1] = self.tree[i << 1][1] + self.tree[i << 1 | 1][1]

    def update(self, i, x):
        i += n-1
        self.tree[i][x % 2] = 1
        self.tree[i][(x+1) % 2] = 0
        while i > 1:
            self.tree[i >> 1][0] = self.tree[i][0] + self.tree[i ^ 1][0]
            self.tree[i >> 1][1] = self.tree[i][1] + self.tree[i ^ 1][1]
            i >>= 1

    def query(self, l, r, ev):
        ret = 0
        l += n-1
        r += n
        while l < r:
            if l & 1:
                ret += self.tree[l][ev]
                l += 1
            if r & 1:
                r -= 1
                ret += self.tree[r][ev]
            l >>= 1
            r >>= 1
        return ret


tree = SegTree()

for _ in range(int(input())):
    q, a, b = map(int, input().split())
    if q == 1:
        tree.update(a, b)
    elif q == 2:
        print(tree.query(a, b, 0))
    else:
        print(tree.query(a, b, 1))
