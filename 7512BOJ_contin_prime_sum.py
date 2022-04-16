isprime = [True]*(10000000)
isprime[0] = isprime[1] = False
for i in range(2, int(10000000**0.5)+1):
    if isprime[i]:
        for j in range(i*i, 10000000, i):
            isprime[j] = False
prime = [x for x in range(2, 10000000) if isprime[x]]

for s in range(int(input())):
    m = int(input())
    now = sum(prime[:m])
    if isprime[now]:
        print('Scenario {}:'.format(s+1))
        print(now)
        continue
    for i in range(m, len(prime)):
        now = now + prime[i] - prime[i-m]
        if isprime[now]:
            print('Scenario {}:'.format(s+1))
            print(now)
            break
