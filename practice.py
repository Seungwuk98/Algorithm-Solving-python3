from random import randint
from collections import defaultdict

m = randint(1, 200000)
qry = []
s = defaultdict(int)
while len(qry) < m:
    a, b = randint(1, 3), randint(1, int(1e9))
    if a == 1:
        s[b] += 1
    elif a == 2 and not s[b]:
        continue
    elif a == 3 and not qry:
        continue
    qry.append([a, b])


print(m)
for x in qry:
    print(*x)
