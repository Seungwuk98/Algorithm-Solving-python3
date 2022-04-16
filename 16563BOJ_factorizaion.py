import sys


def sieve(n):
    sn = int(n**0.5)+1
    mpf = [*range(n+1)]
    for i in range(2, sn+1):
        if mpf[i] == i:
            for j in range(i*i, n+1, i):
                if mpf[j] == j:
                    mpf[j] = i
    return mpf


def factorization(n):
    result = []
    while mpf[n] != n:
        result.append(mpf[n])
        n = n//mpf[n]
    if n != 1:
        result.append(n)
    return sorted(result)


input()
mpf = sieve(5000000)
for x in map(int, input().split()):
    sys.stdout.write(' '.join(map(str, factorization(x))) + '\n')
