a = input()
b = input()
c = len(a)
e = len(b)

d = [0]*(e+1)
idx = [[]for _ in range(c)]
for i in range(c):
    for j in range(e-1, -1, -1):
        if a[i] == b[j]:
            d[j+1] = max(d[:j+1])+1
            idx[i].append(d[j+1])
l = max(d)
print(l)
r = []
for i in range(c-1, -1, -1):
    if l in idx[i]:
        r.append(a[i])
        l -= 1
r.reverse()
print(''.join(r))
