x = input()
p = {'(': 0, '+': 2, '-': 2, '*': 3, '/': 3, ')': 1}
s = []
r = ''
for i in x:
    if i in p:
        while s and p[i]:
            if p[i] <= p[s[-1]]:
                y = s.pop()
                if y != '(':
                    r += y
            elif i == ')' and s[-1] == '(':
                s.pop()
                break
            else:
                break
        if i != ')':
            s.append(i)
    else:
        r += i
r += ''.join(map(str, reversed(s)))
print(r)
