from collections import deque
import sys
input = sys.stdin.readline
s = deque([])
for _ in range(int(input())):
    o = input().rstrip().split()
    c = o[0]
    if c == 'push':
        s.append(o[1])
    elif c == 'front':
        try:
            print(s[0])
        except:
            print(-1)
    elif c == 'back':
        try:
            print(s[-1])
        except:
            print(-1)
    elif c == 'size':
        print(len(s))
    elif c == 'pop':
        try:
            print(s.popleft())
        except:
            print(-1)
    else:
        if not s:
            print(1)
        else:
            print(0)
