import sys
input = sys.stdin.readline
s = [*input().strip('\n')]
boom = [*input().strip('\n')]
l_s = len(s)
l_boom = len(boom)

stack = []
for i in s:
    stack.append(i)
    if len(stack) >= l_boom and boom == stack[-l_boom:]:
        for j in range(l_boom):
            stack.pop()
if not stack:
    print('FRULA')
else:
    print(''.join(stack))
