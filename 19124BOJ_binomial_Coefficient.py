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


n, k = map(int, input().split())
print(comb(n, k, 2, 32))
