n = int(input())
mpf = [*range(n+1)]
sn = int(n**0.5)
for i in range(2, sn+1):
    if mpf[i] == i:
        for j in range(i*i, n+1, i):
            if mpf[j] == j:
                mpf[j] = i

while n != 1:
    print(mpf[n])
    n //= mpf[n]
