from bisect import bisect_left as b
n = int(input())
d = int(1e9)+7
s = [d]*n
l = 0
c = 0
for a in map(int, input().split()):
    f = b(s, a)
    if f >= l:
        l += 1
        c = 1
    elif f == l-1:
        c = (c+1) % d
    s[f] = min(s[f], a)
print(l, c)
