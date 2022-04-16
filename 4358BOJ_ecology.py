import sys
x = sys.stdin.readlines()
lib = {}
for a in x:
    a = a.strip('\n')
    if a not in lib:
        lib[a] = 1
    else:
        lib[a] += 1
ent = sum([*lib.values()])
dic = []
for tree, num in lib.items():
    num /= ent
    dic.append((tree, num))
dic.sort()
for x, y in dic:
    print("{0} {1:0.4f}".format(x, y*100))
