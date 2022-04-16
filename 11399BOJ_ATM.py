from collections import deque
n = int(input())
x = deque(sorted([*map(int, input().split())]))
r = 0
c = 0
for i in x:
    c += i
    r += c
print(r)
