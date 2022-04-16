from cmath import sqrt
from decimal import Decimal


isprime = [True]*42000
isprime[0] = isprime[1] = False
for i in range(2, 205):
    if isprime[i]:
        for j in range(i*i, 42000, i):
            isprime[j] = False

sq = [x*x for x in range(42000) if isprime[x]]
n = len(sq)
K = int(input())


def kth(x, sq):
    ret = 0
    for i1 in range(n):
        if sq[i1] <= x:
            ret += x//sq[i1] - (0 if x % sq[i1] else 1)
            for i2 in range(i1+1, n):
                if sq[i1]*sq[i2] <= x:
                    ret -= x//(sq[i1]*sq[i2]) - (0 if x %
                                                 (sq[i1]*sq[i2]) else 1)
                    for i3 in range(i2+1, n):
                        if sq[i1]*sq[i2]*sq[i3] <= x:
                            ret += x//(sq[i1]*sq[i2]*sq[i3]) - \
                                (0 if x % (sq[i1]*sq[i2]*sq[i3]) else 1)
                            for i4 in range(i3+1, n):
                                if sq[i1]*sq[i2]*sq[i3]*sq[i4] <= x:
                                    ret -= x//(sq[i1]*sq[i2]*sq[i3]*sq[i4]) - \
                                        (0 if x %
                                         (sq[i1]*sq[i2]*sq[i3]*sq[i4]) else 1)
                                    for i5 in range(i4+1, n):
                                        if sq[i1]*sq[i2]*sq[i3]*sq[i4]*sq[i5] <= x:
                                            ret += x//(sq[i1]*sq[i2]
                                                       * sq[i3]*sq[i4]*sq[i5]) - (0 if x % (sq[i1]*sq[i2]*sq[i3]*sq[i4]*sq[i5]) else 1)
                                            for i6 in range(i5+1, n):
                                                if sq[i1]*sq[i2]*sq[i3]*sq[i4]*sq[i5]*sq[i6] <= x:
                                                    ret -= x//(sq[i1]*sq[i2] *
                                                               sq[i3]*sq[i4]*sq[i5]*sq[i6]) - (0 if x % (sq[i1]*sq[i2]*sq[i3]*sq[i4]*sq[i5]*sq[i6]) else 1)
    return ret


def is_sq(x):
    y = Decimal(x)
    if y.sqrt() * y.sqrt() == y:
        return True
    return False


lo, hi = 0, int(1e9)
while lo < hi:
    print(lo, hi)
    mid = lo + hi >> 1
    ret = kth(mid, sq)
    if ret < K:
        lo = mid+1 if is_sq(mid) else mid
    else:
        hi = mid-1
print(lo)
