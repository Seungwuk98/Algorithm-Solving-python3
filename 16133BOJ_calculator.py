from decimal import Decimal as D
v = input()[:-1]

s = []
r = ''
for x in v:
    if '0' <= x <= '9':
        r += x
    else:
        if r:
            s.append(r)
        s.append(x)
        r = ''
if r:
    s.append(r)

o = {'(': 0, ')': 1, '+': 2, '-': 2, '*': 3, '/': 3, '^': 4, '#': 5}
u = []
v = []
for x in s:
    if x in o:
        if x == '#' or x == '^':
            while u and o[u[-1]] > o[x]:
                v.append(u.pop())
        elif x != '(':
            while u and o[u[-1]] >= o[x]:
                v.append(u.pop())
            if x == ')':
                u.pop()
        if x != ')':
            u.append(x)
    else:
        v.append(x)
while u:
    v.append(u.pop())


def w(c, n):
    e = D(1)
    while n != 0:
        if n % 2 == 1:
            e *= c
        c *= c
        n //= 2
    return e


def t(d, r, o):
    if o == '+':
        return d + r
    if o == '-':
        return d - r
    if o == '*':
        return d * r
    if o == '/':
        return D(int(d/r))
    if o == '^':
        return w(d, r)


s = []
for x in v:
    if x in o:
        if x == '#':
            s.append(D(int(s.pop().sqrt())))
        else:
            r = s.pop()
            d = s.pop()
            s.append(t(d, r, x))
    else:
        s.append(D(x))
print(s[0])
