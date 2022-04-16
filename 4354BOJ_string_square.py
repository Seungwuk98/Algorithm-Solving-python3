from sys import stdin
input = stdin.readlines
s = input()


def go_kmp(s):
    l = len(s)
    kmp = [0]*l
    i, j = 0, 1
    while j < l:
        if s[i] == s[j]:
            kmp[j] = i+1
            i += 1
            j += 1
        else:
            if not i:
                kmp[j] = 0
                j += 1
            else:
                i = kmp[i-1]
    return l-kmp[l-1]


for x in s:
    x = x.strip('\n')
    if x != '.':
        a = go_kmp(x)
        print(1 if len(x) % a else len(x)//a)
