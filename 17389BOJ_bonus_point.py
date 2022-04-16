n, s = int(input()), input()
i, r = 0, 0
for j in range(n):
    if s[j] != 'X':
        r += j+i+1
        i += 1
    else:
        i = 0

print(r)
