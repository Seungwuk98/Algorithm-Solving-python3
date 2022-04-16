import sys
from collections import defaultdict
input = sys.stdin.readline
n = int(input())
sn = int(n**0.5)
arr = [*map(int, input().split())]
m = int(input())
qry = []
for i in range(m):
    a, b = map(int, input().split())
    qry.append((a-1, b-1, i))
qry.sort(key=lambda x: (x[0]//sn, x[1]))
result = [0]*m


def madd(x):
    global r
    y = arr[x]
    max_v[now[y]].remove(y)
    now[y] += 1
    max_v[now[y]].add(y)
    if now[y] > r:
        r = now[y]


def mremove(y):
    global r
    y = arr[x]
    max_v[now[y]].remove(y)
    if now[y] == r and not max_v[now[y]]:
        r -= 1
    now[y] -= 1
    max_v[now[y]].add(y)


i, j, k = qry[0]
now = defaultdict(int)
max_v = [set()for _ in range(n)]
max_v[0] = set(arr)
r = 0
for x in range(i, j+1):
    madd(x)
result[k] = r

for w in range(1, m):
    li, lj, lk = qry[w-1]
    ni, nj, nk = qry[w]
    if li//sn == ni//sn:
        if li > ni:
            for x in range(ni, li):
                madd(x)
        else:
            for x in range(li, ni):
                mremove(x)
        for x in range(lj+1, nj+1):
            madd(x)
    else:
        for x in range(li, ni):
            mremove(x)
        if nj > lj:
            for x in range(lj+1, nj+1):
                madd(x)
        else:
            for x in range(nj+1, lj+1):
                mremove(x)
    result[nk] = r

for x in result:
    print(x)
