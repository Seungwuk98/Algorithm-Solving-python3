r = []

for _ in range(int(input())):
    l = [0]*7
    d = sorted([*map(int, input().split())])
    s = len(set(d))
    for i in d:
        l[i] += 1
    if s == 1:
        r.append(50000+5000*d[0])
    elif s == 2:
        if 3 in l:
            r.append(10000+1000*l.index(3))
        else:
            r.append(2000)
            for i in range(7):
                if l[i] != 0:
                    r[-1] += i*500
    elif s == 3:
        r.append(1000+100*l.index(2))
    elif s == 4:
        r.append(d[-1]*100)

print(max(r))
