from collections import deque
import sys
input = sys.stdin.readline
s = []
for _ in range(int(input())):
    o = input().rstrip().split()
    c = o[0]
    if c == 'push':
        s.append(o[1])
    elif c == 'top':
        try:
            print(s[-1])
        except:
            print(-1)
    elif c == 'size':
        print(len(s))
    elif c == 'pop':
        try:
            print(s.pop())
        except:
            print(-1)
    else:
        if not s:
            print(1)
        else:
            print(0)
