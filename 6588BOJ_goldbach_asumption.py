import sys
input = sys.stdin.readline

a = [True]*(1000001)
a[0] = a[1] = False
for i in range(2, 1001):
    if a[i]:
        for j in range(i*i, 1000001, i):
            a[j] = False
p = [x for x in range(1000001) if a[x]]

while True:
    n = int(input())
    if not n:
        break
    r = False
    for x in p:
        if x > n//2:
            break
        if a[n-x]:
            r = True
            print('{} = {} + {}'.format(n, x, n-x))
            break
