A = int(input())
X = int(input())


def divide(A, X):
    if X == 1:
        return A

    if X % 2 == 0:
        return (divide(A, X//2)**2) % 1000000007
    else:
        return (divide(A, X//2)**2*A) % 1000000007


print(divide(A, X))

C = int(input())
n = int(input())


def fpow(C, n):
    if n == 1:
        return C
    result = 1
    while n:
        if n & 1:
            result = (result*C) % 1000000007
        C = (C*C) % 1000000007
        n >>= 1
    return result


print(fpow(C, n))
