import sys
input = sys.stdin.readline


def pd(s, i, j):
    while i < j:
        if s[i] != s[j]:
            return False
        i += 1
        j -= 1
    return True


def pspd(s):
    i = 0
    j = len(s)-1
    while i < j:
        if s[i] != s[j]:
            if pd(s, i+1, j) or pd(s, i, j-1):
                return 1
            else:
                return 2
        i += 1
        j -= 1
    return 0


for _ in range(int(input())):
    print(pspd(input().strip('\n')))
