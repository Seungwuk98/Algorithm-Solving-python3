import sys
input = sys.stdin.readline

t = input().strip('\n')
p = input().strip('\n')


i, j = 0, 1
kmp = [0]*len(p)
while j < len(p):
    if p[i] != p[j]:
        if not i:
            j += 1
        else:
            i = kmp[i-1]
    else:
        kmp[j] = i+1
        i += 1
        j += 1
r = 0
r_l = []

i, j = 0, 0
while i < len(t):
    if t[i] != p[j]:
        if not j:
            i += 1
        else:
            j = kmp[j-1]
    else:
        i += 1
        j += 1
        if j == len(p):
            r += 1
            r_l.append(i-len(p)+1)
            j = kmp[j-1]
print(r)
for _ in r_l:
    print(_, end=' ')
