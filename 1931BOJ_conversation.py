import sys
input = sys.stdin.readline
n = int(input())
c = sorted([[*map(int, input().split())]
           for _ in range(n)])
c.sort(key=lambda x: x[1])
now_end = 0
r = 0
for i in c:
    s, e = i
    if s >= now_end:
        r += 1
        now_end = e
print(r)
