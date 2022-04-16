s, j = input(), 0
for i in range(len(s)-1):
    if s[i] != s[i+1]:
        j += 1

print((j+1)//2)
