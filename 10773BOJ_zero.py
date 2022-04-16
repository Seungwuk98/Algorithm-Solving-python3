import sys
input = sys.stdin.readline
s = []
for _ in range(int(input())):
    x = int(input())
    if x == 0:
        s.pop()
    else:
        s.append(x)
print(sum(s))
