D = 142857


def prep(n, p, q):
    pq = p**q
    fact = [1]*(n+1)
    for i in range(2, n+1):
        if i % p:
            fact[i] = fact[i-1]*i % pq
        else:
            fact[i] = fact[i-1]
    return fact


def modpow(c, n, d):
    r = 1
    while n:
        if n & 1:
            r = r*c % d
        c = c*c % d
        n >>= 1
    return r


def comb(n, r, p, q):
    pq = p**q
    fact = prep(pq-1, p, q)

    def em(n):
        if n < pq:
            k = n//p
            return k, fact[n]
        k = n//p
        t, s = divmod(n, pq)
        ne, nm = em(k)
        e = k+ne
        m = nm*modpow(fact[pq-1], t, pq)*fact[s] % pq
        return e, m

    e1, m1 = em(n)
    e2, m2 = em(r)
    e3, m3 = em(n-r)
    e = e1-e2-e3
    if e:
        return 0
    for i in range(pq):
        if m2*m3*i % pq == 1:
            break
    return m1*i % pq


for _ in range(int(input())):
    n, r = map(int, input().split())
    a = comb(n, r, 3, 3)
    b = comb(n, r, 11, 1)
    c = comb(n, r, 13, 1)
    d = comb(n, r, 37, 1)
    print(a, b, c, d)
    result = (a*5291*26 % D + b*12987*8 %
              D + c*10989*10 % D + d*3861*20 % D) % D
    print(result)


def fact(n):
    return 1 if not n else n*fact(n-1)


print(fact(10)//fact(3)//fact(7) % 27)
