import sys
input = sys.stdin.readline


def D(n):
    return (2*n) % 10000


def S(n):
    return (n-1) % 10000


def L(n):
    x = n//1000
    return (n % 1000)*10 + x


def R(n):
    x = n % 10
    return n//10 + x*1000


dslr = ['D', 'S', 'L', 'R']

for _ in range(int(input())):
    a, b = map(int, input().split())
    check = [False]*10001
    dp = ['']*10001
    idx = [(a, '')]
    while not check[b]:
        tmp = []
        for i, o in idx:
            x = (D(i), S(i), L(i), R(i))
            for j in range(4):
                if check[x[j]]:
                    continue
                check[x[j]] = True
                dp[x[j]] = o+dslr[j]
                tmp.append((x[j], dp[x[j]]))
        idx = tmp
    print(dp[b])
