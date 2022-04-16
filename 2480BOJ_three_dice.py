l = [0]*7
for i in map(int, input().split()):
    l[i] += 1
if max(l) == 3:
    print(10000 + 1000*(l.index(3)))
elif max(l) == 2:
    print(1000 + 100*(l.index(2)))
else:
    for i in range(6, 0, -1):
        if l[i] != 0:
            print(100*i)
            break
