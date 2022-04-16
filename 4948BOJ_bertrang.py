from bisect import *
isprime = [True]*(250000)
isprime[0] = isprime[1] = False
for i in range(2, 501):
    if isprime[i]:
        for j in range(i*i, 250000, i):
            isprime[j] = False
prime = [x for x in range(250000) if isprime[x]]

while True:
    n = int(input())
    if not n:
        break
    print(bisect_right(prime, 2*n) - bisect_right(prime, n))
