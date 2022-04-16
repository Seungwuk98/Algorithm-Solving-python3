import io
import os
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline


class Node:
    def __init__(self) -> None:
        self.child = [False]*2
        self.visit = 0

    def insert(self, num, i):
        if i == -1:
            return
        c = 1 if num & (1 << i) else 0
        if not self.child[c]:
            self.child[c] = Node()
        self.child[c].visit += 1
        self.child[c].insert(num, i-1)

    def delete(self, num, i):
        if i == -1:
            return
        c = 1 if num & (1 << i) else 0
        self.child[c].visit -= 1
        self.child[c].delete(num, i-1)
        if not self.child[c].visit:
            self.child[c] = False

    def xor(self, num, i):
        if i == -1:
            return 0
        c = 0 if num & (1 << i) else 1
        if self.child[c]:
            return (1 << i) + self.child[c].xor(num, i-1)
        else:
            return self.child[(c+1) % 2].xor(num, i-1)


m = int(input())
root = Node()
root.insert(0, 30)
for _ in range(m):
    a, b = map(int, input().split())
    if a == 1:
        root.insert(b, 30)
    elif a == 2:
        root.delete(b, 30)
    else:
        print(root.xor(b, 30))
