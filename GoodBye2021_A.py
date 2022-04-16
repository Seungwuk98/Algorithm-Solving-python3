from bisect import bisect_right
isprime = [True]*(10001)
isprime[0] = isprime[1] = False
for i in range(2, 101):
    if isprime[i]:
        for j in range(i*i, 10001, i):
            isprime[j] = False
prime = [x for x in range(10001) if isprime[x]]
pre = []
for i in range(len(prime)-1):
    pre.append(prime[i]*prime[i+1])
n = int(input())
print(pre[bisect_right(pre, n)])
