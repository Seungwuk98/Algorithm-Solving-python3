import sys
input = sys.stdin.readline

n = int(input())
sn = int(n**0.5)+1
arr = [*map(int, input().split())]
base_str = [str(i)+'\n' for i in range(100001)]


class Node:
    def __init__(self, lo, hi) -> None:
        self.lo = lo
        self.hi = hi
        self.cnt = 0
        self.left = self.right = None


class Segtree:
    def __init__(self) -> None:
        self.tree = [0]*20002

    def update(self, p, i):
        self.update1(p, -1)
        self.update1(i, 1)

    def update1(self, i, z):
        i += 10001
        self.tree[i] += z
        while i >> 1:
            self.tree[i >> 1] = self.tree[i] + self.tree[i ^ 1]
            i >>= 1

    def query(self, l, r):
        l += 10001
        r += 10002
        ret = 0
        while l < r:
            if l & 1:
                ret += self.tree[l]
                l += 1
            if r & 1:
                r -= 1
                ret += self.tree[r]
        return ret


trees = [Segtree()for _ in range(sn)]
for i in range(n):
    trees[i//sn].update(arr[i], 1)

for _ in range(int(input())):
    qry = [*map(int, input().split())]
    if qry[0] == 1:
        idx = qry[1]-1
        trees[idx//sn].update(arr[idx], qry[2])
        arr[idx] = qry[2]
    else:
        i, j, k = qry[1]-1, qry[2]-1, qry[3]
        ret = 0
        if i//sn != j//sn:
            for x in range(i, min((i//sn+1)*sn, n)):
                if arr[x] > k:
                    ret += 1
            for x in range(j//sn*sn, j+1):
                if arr[x] > k:
                    ret += 1
            for y in range(i//sn+1, j//sn):
                ret += trees[y].query(k+1, 10000)
        else:
            for x in range(i, j+1):
                if arr[x] > k:
                    ret += 1
        sys.stdout.write(base_str[ret])
