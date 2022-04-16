n = int(input())
eratos = [True]*(n+1)
primenumber = []
prefix = [0]
r = 0

for i in range(2, n+1):
    if eratos[i]:
        prefix.append(i+prefix[-1])
        primenumber.append(i)
    if i < int(n**0.5)+1 and eratos[i]:
        x = i*2
        while x <= n:
            eratos[x] = False
            x += i

i, j = 0, 1
r = 0
l = len(prefix)-1
while True:
    if (j == l and prefix[j]-prefix[i] < n) or i == l:
        break

    if prefix[j]-prefix[i] < n:
        j = min(j+1, l)
    elif prefix[j]-prefix[i] > n:
        i += 1
    else:
        r += 1
        i += 1
        j = min(j+1, l)
print(r)
