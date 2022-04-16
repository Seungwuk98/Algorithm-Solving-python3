import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
sn = int((n+1)**0.5)+1
arr = [*map(int, input().split())]
pre = [0]*(n+1)
MAX = 0
MIN = 0
for i in range(n):
    pre[i+1] = pre[i]+arr[i]
    MAX = max(MAX, pre[i+1])
    MIN = min(MIN, pre[i+1])
cnt = [0]*(n+1)
cnt_sq = [0]*(sn+1)
idx = [deque()for _ in range(MAX-MIN+1)]
m = int(input())
qry = []
for i in range(m):
    a, b = map(int, input().split())
    qry.append((a-1, b, i))
qry.sort(key=lambda x: (x[0]//sn, x[1]))


def insert(x):
    y = pre[x]
    d = idx[y]
    if not d:
        cnt[0] += 1
        cnt_sq[0] += 1
        d.append(x)
    else:
        lm = d[-1]-d[0]
        if x < d[0]:
            d.appendleft(x)
        else:
            d.append(x)
        nm = d[-1]-d[0]
        cnt[lm] -= 1
        cnt_sq[lm//sn] -= 1
        cnt[nm] += 1
        cnt_sq[nm//sn] += 1


def delete(x):
    y = pre[x]
    d = idx[y]
    lm = d[-1]-d[0]
    if x == d[0]:
        d.popleft()
    else:
        d.pop()
    cnt[lm] -= 1
    cnt_sq[lm//sn] -= 1
    if d:
        nm = d[-1]-d[0]
        cnt[nm] += 1
        cnt_sq[nm//sn] += 1


def find_max():
    for i in range(sn, -1, -1):
        if cnt_sq[i]:
            break
    for j in range(min(n, (i+1)*sn), i*sn-1, -1):
        if cnt[j]:
            return j


li, lj, lk = qry[0]
for x in range(li, lj+1):
    insert(x)
result = [0]*m
result[lk] = find_max()

for w in range(1, m):
    li, lj, lk = qry[w-1]
    ni, nj, nk = qry[w]
    if li//sn == ni//sn:
        for x in range(lj+1, nj+1):
            insert(x)
        if li < ni:
            for x in range(li, ni):
                delete(x)
        else:
            for x in range(li-1, ni-1, -1):
                insert(x)
    else:
        if lj < nj:
            for x in range(lj+1, nj+1):
                insert(x)
        else:
            for x in range(lj, nj, -1):
                delete(x)
        for x in range(li, ni):
            delete(x)
    result[nk] = find_max()
for x in result:
    print(x)
