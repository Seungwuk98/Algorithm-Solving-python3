from collections import deque
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
sn = int(n**0.5)+1
arr = [*map(int, input().split())]
m = int(input())
qry = []
for i in range(m):
    a, b = map(int, input().split())
    qry.append((a-1, b-1, i))
qry.sort(key=lambda x: (x[0]//sn, x[1]))

cnt = [0]*n
cnt_sq = [0]*sn
idx = [deque()for _ in range(k+1)]


def insert(x):
    y = arr[x]
    d = idx[y]
    if not d:
        d.append(x)
        cnt[0] += 1
        cnt_sq[0] += 1
    else:
        l_m = d[-1]-d[0]
        if x < d[0]:
            d.appendleft(x)
        else:
            d.append(x)
        n_m = d[-1]-d[0]
        cnt[l_m] -= 1
        cnt_sq[l_m//sn] -= 1
        cnt[n_m] += 1
        cnt_sq[n_m//sn] += 1


def delete(x):
    y = arr[x]
    d = idx[y]
    l_m = d[-1]-d[0]
    if x == d[0]:
        d.popleft()
    else:
        d.pop()
    cnt[l_m] -= 1
    cnt_sq[l_m//sn] -= 1
    if d:
        n_m = d[-1]-d[0]
        cnt[n_m] += 1
        cnt_sq[n_m//sn] += 1


def find_max():
    for i in range(sn-1, -1, -1):
        if cnt_sq[i]:
            break
    for j in range((i+1)*sn, i*sn-1, -1):
        if j < n and cnt[j]:
            return j


result = [0]*m
ll, lr, lk = qry[0]
for x in range(ll, lr+1):
    insert(x)
result[lk] = find_max()

for w in range(1, m):
    ll, lr, lk = qry[w-1]
    nl, nr, nk = qry[w]
    if ll//sn == nl//sn:
        for x in range(lr+1, nr+1):
            insert(x)
        if ll < nl:
            for x in range(ll, nl):
                delete(x)
        else:
            for x in range(ll-1, nl-1, -1):
                insert(x)
    else:
        if lr < nr:
            for x in range(lr+1, nr+1):
                insert(x)
        else:
            for x in range(lr, nr, -1):
                delete(x)
        for x in range(ll, nl):
            delete(x)
    result[nk] = find_max()
for x in result:
    print(x)
