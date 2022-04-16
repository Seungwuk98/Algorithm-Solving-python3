def find(arr):
    if not arr:
        return set()
    n = (1 << (len(arr)))-1
    c = n
    r = []
    while c:
        s = 0
        for x in trav(c):
            s += arr[x]
        r.append(s)
        c = n & (c-1)
    r.sort()
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


n, s = map(int, input().split())
x = find([*map(int, input().split())])
print(x.count(s))
