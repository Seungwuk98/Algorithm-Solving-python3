import sys
input = sys.stdin.readline
n, m = map(int, input().split())
d = {}
r = {}
for i in range(1, n+1):
    n = input().rstrip()
    d[n] = i
    r[i] = n

for _ in range(m):
    n = input().rstrip()
    try:
        n = int(n)
        print(r[n])
    except:
        print(d[n])
