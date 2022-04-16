import sys
input = sys.stdin.readline
n, m = map(int, input().split())
a = set([input().rstrip()for _ in range(n)])
b = set([input().rstrip()for _ in range(m)])
c = sorted(list(a & b))
l = len(c)
print(l)
for x in c:
    print(x)
