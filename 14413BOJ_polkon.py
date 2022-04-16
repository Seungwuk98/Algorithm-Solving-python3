from glob import glob
import sys
from bisect import bisect_left
input = sys.stdin.readline

n, q = map(int, input().split())
sn = int(n**0.5)+1
arr = [*map(int, input().split())]
nums = sorted(arr)
for i in range(n):
    arr[i] = bisect_left(nums, arr[i])

qry = []
for i in range(q):
    x, y = map(int, input().split())
    qry.append((x-1, y-1, i))
qry.sort(key=lambda x: (x[0]//sn, x[1]))

now = [0]*n
two = 0


def insert(x):
    global two
    y = arr[x]
    if now[y] == 2:
        two -= 1
    now[y] += 1
    if now[y] == 2:
        two += 1


def remove(x):
    global two
    y = arr[x]
    if now[y] == 2:
        two -= 1
    now[y] -= 1
    if now[y] == 2:
        two += 1


result = [0]*q
li, lj, lk = qry[0]
for x in range(li, lj+1):
    insert(x)
result[lk] = two

for w in range(1, q):
    ni, nj, nk = qry[w]
    if li//sn == ni//sn:
        for x in range(lj+1, nj+1):
            insert(x)
        if li < ni:
            for x in range(li, ni):
                remove(x)
        else:
            for x in range(ni, li):
                insert(x)
    else:
        if lj < nj:
            for x in range(lj+1, nj+1):
                insert(x)
        else:
            for x in range(nj+1, lj+1):
                remove(x)
        for x in range(li, ni):
            remove(x)
    result[nk] = two
    li, lj, lk = ni, nj, nk
for x in result:
    print(x)
