n = int(input())


def star(n):
    if n == 1:
        return ['  *  ', ' * * ', '*****']

    s = star(n//2)
    l = len(s)
    t = []
    for i in s:
        t.append(i+' '+i)
    for i in range(l):
        s[i] = ' '*l + s[i]+' '*l
    s.extend(t)
    return s


print('\n'.join(star(n//3)))
