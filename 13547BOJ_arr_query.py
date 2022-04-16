import sys
input = sys.stdin.readline

n = int(input())
sn = int(n**0.5)+1
arr = [*map(int, input().split())]
m = int(input())

qry = []
for i in range(m):
    x, y = map(int, input().split())
    qry.append((x-1, y-1, i))
qry.sort(key=lambda x: (x[0]//sn, x[1]))

now = 0
buk = [0]*1000001


def insert(x):
    global now
    y = arr[x]
    if not buk[y]:
        now += 1
    buk[y] += 1


def remove(x):
    global now
    y = arr[x]
    buk[y] -= 1
    if not buk[y]:
        now -= 1


result = [0]*m
li, lj, lk = qry[0]
for x in range(li, lj+1):
    insert(x)
result[lk] = now

for w in range(1, m):
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
    result[nk] = now
    li, lj, lk = ni, nj, nk
print('\n'.join(map(str, result)))
