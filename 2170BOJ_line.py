import sys
input = sys.stdin.readline
n = int(input())
line = [[*map(int, input().split())]for _ in range(n)]
line.sort()
s = []
result = 0
for l, r in line:
    if not s:
        s.append((l, r))
    elif s[-1][1] >= l:
        pl, pr = s.pop()
        s.append((pl, max(r, pr)))
    else:
        pl, pr = s.pop()
        result += pr-pl
        s.append((l, r))
pl, pr = s[0]
result += pr-pl
print(result)
