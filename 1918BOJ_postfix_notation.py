from collections import deque


s = input()


def postfix_notation(s):
    q = deque([])
    c = 0
    g = ''
    for i in s:
        if c:
            if i == '(':
                c += 1
                g += i
            elif i == ')':
                c -= 1
                if not c:
                    g += ')'
                    q.append(postfix_notation(g[1:-1]))
                    g = ''
                else:
                    g += i
            else:
                g += i
        else:
            if i == '(':
                c += 1
                g += i
            else:
                q.append(i)
    q2 = deque([])
    while q:
        i = q.popleft()
        if not q2:
            q2.append(i)
        elif q2[-1] == '*' or q2[-1] == '/':
            x1, x2 = q2.pop(), q2.pop()
            q2.append('('+x2+x1+i+')')
        else:
            q2.append(i)
    q3 = deque([])
    while q2:
        i = q2.popleft()
        if not q3:
            q3.append(i)
        elif q3[-1] == '+' or q3[-1] == '-':
            x1, x2 = q3.pop(), q3.pop()
            q3.append('('+x2+x1+i+')')
        else:
            q3.append(i)
    return ''.join(map(str, q3))


x = postfix_notation(s)
q = deque([])
stack = []
for i in x:
    if i == '(':
        continue
    elif 'A' <= i <= 'Z':
        q.append(i)
    elif i == ')':
        x2, x1 = q.pop(), q.pop()
        o = stack.pop()
        q.append(x1+x2+o)
    else:
        stack.append(i)
print(''.join(map(str, q)))
