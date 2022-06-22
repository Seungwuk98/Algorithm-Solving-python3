n = int(input())
s = [input()for _ in range(n)]
m = len(s[0])
ans = ['?']*m
for i in range(m):
    c = s[0][i]
    for j in range(1, n):
        if c != s[j][i]:
            c = '?'
    ans[i] = c
print(''.join(ans))
