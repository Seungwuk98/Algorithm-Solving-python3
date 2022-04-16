l = int(input())
s = input()
k = [0]*l
i, j = 0, 1
while j < l:
    if s[i] == s[j]:
        k[j] = i+1
        i += 1
        j += 1
    else:
        if not i:
            k[j] = 0
            j += 1
        else:
            i = k[i-1]
print(l-k[l-1])
