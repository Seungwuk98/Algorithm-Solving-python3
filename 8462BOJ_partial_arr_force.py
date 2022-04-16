import os
import io
from collections import defaultdict
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

n, t = map(int, input().split())
sn = int(n**0.5+1)
now = defaultdict(int)
arr = [*map(int, input().split())]
qry = []
for i in range(t):
    l, r = map(int, input().split())
    qry.append((l-1, r-1, i))
qry.sort(key=lambda x: (x[0]//sn, x[1]))


def insert(x):
    global force
    y = arr[x]
    force -= now[y]*now[y]*y
    now[y] += 1
    force += now[y]*now[y]*y


def delete(x):
    global force
    y = arr[x]
    force -= now[y]*now[y]*y
    now[y] -= 1
    force += now[y]*now[y]*y


ll, lr, lk = qry[0]
force = 0

for x in range(ll, lr+1):
    insert(x)
result = [0]*t
result[lk] = force


for w in range(1, t):
    ll, lr, lk = qry[w-1]
    nl, nr, nk = qry[w]
    if ll//sn == nl//sn:
        for x in range(lr+1, nr+1):
            insert(x)
        if ll < nl:
            for x in range(ll, nl):
                delete(x)
        else:
            for x in range(nl, ll):
                insert(x)
    else:
        if lr < nr:
            for x in range(lr+1, nr+1):
                insert(x)
        else:
            for x in range(nr+1, lr+1):
                delete(x)
        for x in range(ll, nl):
            delete(x)
    result[nk] = force
for x in result:
    print(x)
