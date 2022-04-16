import sys
input = sys.stdin.readline


def find():
    s = []
    result = 0
    for i in range(n):
        y = i
        while s and s[-1][0] > arr[i]:
            x, y = s.pop()
            result = max(result, x*(i-y))
        s.append((arr[i], y))
    while s:
        x, y = s.pop()
        result = max(result, x*(n-y))
    return result


while True:
    arr = [*map(int, input().split())]
    n = arr.pop(0)
    if not n:
        break
    print(find())
