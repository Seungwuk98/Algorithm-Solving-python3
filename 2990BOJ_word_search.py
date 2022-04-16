import sys
input = sys.stdin.readline
AL = 27


def num(a):
    return ord(a)-97


class Node:
    __slots__ = ['child', 'end', 'visit']

    def __init__(self) -> None:
        self.child = [None]*AL
        self.end = n-1
        self.visit = 0

    def insert(self, s, i, idx):
        if len(s) == i:
            self.end = idx
            if not self.child[26]:
                self.child[26] = Node()
            self.child[26].visit += 1
            return
        code = num(s[i])
        if not self.child[code]:
            self.child[code] = Node()
        self.child[code].visit += 1
        self.child[code].insert(s, i+1, idx)

    def find1(self, s, i):
        if len(s) == i:
            return self.end
        code = num(s[i])
        if not self.child[code]:
            return n-1
        return self.child[code].find1(s, i+1)

    def find2(self, s, i):
        result = 0
        for node in self.child:
            if node:
                result += node.visit
        if len(s) == i:
            return result
        code = num(s[i])
        if self.child[code]:
            result += self.child[code].find2(s, i+1)
        return result


n = int(input())
root = Node()
word = []
for i in range(n):
    s = input().strip('\n')
    root.insert(s, 0, i)
    word.append(s)


search = []
q = int(input())
for i in range(q):
    s = input().strip('\n')
    search.append((s, i))

idx = {x[0]: root.find1(x[0], 0)for x in search}
search.sort(key=lambda x: idx[x[0]])
result = [0]*q
li = -1
new = Node()
for x in search:
    search, k = x
    ni = idx[search]
    for i in range(li+1, ni+1):
        new.insert(word[i], 0, i)
    li = ni
    result[k] = new.find2(search, 0)

for x in result:
    print(x)
