import sys
input = sys.stdin.readline


def p(n):
    s = 'I'
    for i in range(n):
        s += 'OI'
    return s


s = p(int(input()))
kmp = [0]*len(s)

i, j = 0, 1
while j < len(s):
    if s[i] != s[j]:
        if not i:
            j += 1
        else:
            i = 0
    else:
        kmp[j] = i+1
        i += 1
        j += 1
m = int(input())
com = input()

i = 0
j = 0
r = 0
while i < len(com):
    if com[i] != s[j]:
        if not j:
            i += 1
        else:
            j = kmp[j-1]
    else:
        i += 1
        j += 1
        if j == len(s):
            r += 1
            j = kmp[j-1]
print(r)
