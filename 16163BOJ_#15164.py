s = input()
s = '#'.join([*s])
n = len(s)
d = [0]*n
p = 0
v = 0
for i in range(1, n):
    if i <= v:
        d[i] = min(d[2*p-i], v-i)
    while i-d[i]-1 >= 0 and i+d[i]+1 < n and s[i-d[i]-1] == s[i+d[i]+1]:
        d[i] += 1
    if i+d[i] > v:
        v = i+d[i]
        p = i
for i in range(n):
    d[i] += +((i & 1) == (d[i] & 1))
print(max(d))
