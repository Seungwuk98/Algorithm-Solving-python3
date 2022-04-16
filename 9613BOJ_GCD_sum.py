from itertools import combinations


def gcd(a, b):
    return a if not b else gcd(b, a % b)


for _ in range(int(input())):
    arr = [*map(int, input().split())]
    arr.pop(0)
    comb = combinations(arr, 2)
    result = 0
    for x, y in comb:
        result += gcd(x, y)
    print(result)
