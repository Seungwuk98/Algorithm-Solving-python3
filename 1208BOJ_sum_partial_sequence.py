from collections import defaultdict
n, s = map(int, input().split())
arr = [*map(int, input().split())]


def find(arr):
    if not arr:
        return []
    n = (1 << (len(arr)))-1
    c = n
    r = []
    while c:
        s = 0
        for x in trav(c):
            s += arr[x]
        r.append(s)
        c = n & (c-1)
    return r


def trav(bit):
    r = []
    i = 0
    while bit:
        if bit & 1:
            r.append(i)
        bit >>= 1
        i += 1
    return r


a = find(arr[:n//2])
b = find(arr[n//2:])
r = 0
r += a.count(s) + b.count(s)
c = defaultdict(int)
for y in b:
    c[y] += 1
for x in a:
    r += c[s-x]
print(r)
