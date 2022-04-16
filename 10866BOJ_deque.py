from collections import deque
import sys
input = sys.stdin.readline
s = deque([])
for _ in range(int(input())):
    o = input().rstrip().split()
    c = o[0]
    if c == 'push_front':
        s.appendleft(o[1])
    elif c == 'push_back':
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
    elif c == 'pop_front':
        try:
            print(s.popleft())
        except:
            print(-1)
    elif c == 'pop_back':
        try:
            print(s.pop())
        except:
            print(-1)
    else:
        if not s:
            print(1)
        else:
            print(0)
