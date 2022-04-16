import sys
p = sys.stdout.write
n, k = map(int, input().split())
a = [i for i in range(1, n+1)]
r = []
i = 0
while len(a) != 0:
    i = (i+k-1) % len(a)
    r.append(str(a.pop(i)))
p('<')
p(', '.join(r))
p('>')
