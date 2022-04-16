import sys
input = sys.stdin.readline
n = int(input())
c1 = sorted([*map(int, input().split())])
c2 = sorted([*map(int, input().split())])
i1 = [0]*n
i2 = [0]*n
d = 360000
for i in range(-1, n-1):
    i1[i] = (c1[i+1] - c1[i]) % d
    i2[i] = (c2[i+1] - c2[i]) % d

kmp = [0]*n
i, j = 0, 1
while j < n:
    if i1[i] == i1[j]:
        kmp[j] = i+1
        i += 1
        j += 1
    else:
        if not i:
            kmp[j] = 0
            j += 1
        else:
            i = kmp[i-1]
check = False
i = j = k = 0
while j < 2*n:
    if i1[i] == i2[k]:
        i += 1
        j += 1
        k = j % n
        if i == n:
            check = True
            break
    else:
        if not i:
            j += 1
            k = j % n
        else:
            i = kmp[i-1]

if check:
    print('possible')
else:
    print('impossible')
