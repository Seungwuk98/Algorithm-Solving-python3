from collections import deque


def gcd(x, y):
    return x if y == 0 else gcd(y, x % y)


def l(x, y):
    return x*y//gcd(x, y)


def solution(wave1, wave2):
    c1, c2 = check(wave1), check(wave2)
    wave1 = wave1[:c1]
    wave2 = wave2[:c2]
    ll = l(len(wave1), len(wave2))
    w1 = []
    while len(w1) != ll:
        w1.extend(wave1)
    w2 = []
    while len(w2) != ll:
        w2.extend(wave2)
    w1 = deque(w1)
    result = int(1e15)
    for i in range(ll):
        w1.append(w1.popleft())
        result = min(result, cal(w1, w2))
        if not result:
            return result
    return result


def cal(wave1, wave2):
    n = len(wave1)
    w = [wave1[i]+wave2[i] for i in range(n)]
    c = check(w)
    if c == 1:
        return 0
    else:
        return sum([x*x for x in w])//(n//c)


def check(w):
    n = len(w)
    k = [0]*n
    i, j = 0, 1
    while j < n:
        if w[i] == w[j]:
            k[j] = i+1
            i += 1
            j += 1
        else:
            if not i:
                k[j] = 0
                j += 1
            else:
                i = k[i-1]
    return n-k[n-1]


wave1, wave2 = [1, 2, 2, 1, 1, 2], [-2, -1]
print(solution(wave1, wave2))
wave1, wave2 = [2, -1, 3], [-1, -1]
print(solution(wave1, wave2))
wave1, wave2 = [0, 1, 1, 1, 1, 1, ], [0, 0, 1, 0, 0, 0]
print(solution(wave1, wave2))
wave1, wave2 = [2, 0, 1, 1, 1, 0], [0, 0, -1]
print(solution(wave1, wave2))
