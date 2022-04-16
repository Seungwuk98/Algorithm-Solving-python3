from collections import deque
n = int(input())


d = set([i*i for i in range(1, int(n**0.5)+1)])

q = deque([(n, 0)])

if n in d:
    print(1)
    exit(0)

x = set()
for i in d:
    if n-i in d:
        print(2)
        exit(0)
    else:
        x.add(n-i)

y = set()
for i in x:
    for j in d:
        if i-j in d:
            print(3)
            exit(0)
        else:
            y.add(i-j)

print(4)
