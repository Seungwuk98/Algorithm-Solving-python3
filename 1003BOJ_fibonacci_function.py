def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    a, b = 0, 1
    for i in range(n-1):
        a, b = b, a+b
    return b


for _ in range(int(input())):
    count = [0, 0]
    n = int(input())
    print(fibonacci(n-1), fibonacci(n))
