import sys
input = sys.stdin.readline
r = 0
s = []
for _ in range(int(input())):
    b = int(input())
    x = 1
    while s and s[-1][0] <= b:
        prev, num = s.pop()
        if prev == b:
            x += num
        r += num
    if s:
        r += 1
    s.append((b, x))
print(r)
