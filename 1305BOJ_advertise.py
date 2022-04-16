l = int(input())
s = input()

kmp = [0]*l

i, j = 0, 1
while j < l:
    if s[i] == s[j]:
        kmp[j] = i+1
        i += 1
        j += 1
    elif not i:
        kmp[j] = 0
        j += 1
    else:
        i = kmp[i-1]
print(l - kmp[l-1])
