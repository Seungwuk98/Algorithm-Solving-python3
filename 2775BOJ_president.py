x = [i for i in range(15)]
y = [x] + [[0]*15 for i in range(14)]


def h(k, n):
    if y[k][n] != 0:
        return y[k][n]
    if k == 1:
        return sum(x[1:n+1])
    else:
        a = 0
        for i in range(1, n+1):
            a += h(k-1, i)
        y[k][n] = a
        return a


for _ in range(int(input())):
    k = int(input())
    n = int(input())
    print(h(k, n))
