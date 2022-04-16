n = int(input())
arr = sorted([*map(int, input().split())])
D = 1000000007


def pow(c, n):
    r = 1
    while n:
        if n & 1:
            r = r*c % D
        c = c*c % D
        n >>= 1
    return r


result = 0
for i in range(n):
    result = (result + arr[i]*pow(2, i)) % D
    result = (result - arr[i]*pow(2, n-i-1)) % D
print(result)
