from bisect import *
isprime = [True]*10001
isprime[0] = isprime[1] = False
for i in range(1, 101):
    if isprime[i]:
        for j in range(i*i, 10001, i):
            isprime[j] = False

prime = [x for x in range(10001) if isprime[x]]
l = bisect_left(prime, int(input()))
r = bisect_right(prime, int(input()))
if l == r:
    print(-1)
else:
    print(sum(prime[l:r]))
    print(prime[l])
