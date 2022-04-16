import sys
input = sys.stdin.readline
a = set()

for _ in range(int(input())):
    o = input().split()
    x = o[0]
    if x == 'add':
        a.add(o[1])
    elif x == 'remove':
        if o[1] in a:
            a.remove(o[1])
    elif x == 'check':
        print(+(o[1] in a))
    elif x == 'toggle':
        if o[1] in a:
            a.remove(o[1])
        else:
            a.add(o[1])
    elif x == 'all':
        a = set([str(i) for i in range(1, 21)])
    else:
        a = set()
