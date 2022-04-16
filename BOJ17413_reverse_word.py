from collections import deque
import sys
print = sys.stdout.write
s = input()

q = deque([])
stack = []

for i in s:
    if i == '<' and not stack:
        q.append(i)
    elif i == '>':
        for j in range(len(q)):
            print(q.popleft())
        print('>')
    elif q:
        q.append(i)
    elif i == ' ':
        for j in range(len(stack)):
            print(stack.pop())
        print(' ')
    elif i == '<':
        for j in range(len(stack)):
            print(stack.pop())
        q.append(i)
    else:
        stack.append(i)
for j in range(len(stack)):
    print(stack.pop())
