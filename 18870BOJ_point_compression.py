import sys
input = sys.stdin.readline
n = int(input())
y = []
for idx, x in enumerate([*map(int, input().split())]):
    y.append((x, idx))
r = [0]*n
y.sort()
for i in range(len(y)-1):
    x1, idx1 = y[i]
    x2, idx2 = y[i+1]
    if x1 != x2:
        r[idx2] = r[idx1] + 1
    else:
        r[idx2] = r[idx1]
print(*r)
