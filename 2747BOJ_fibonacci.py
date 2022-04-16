import sys

fibonacciList = [0, 1]


def fibonacci(n):
    if len(fibonacciList)-1 < n:
        fibonacciList.append(fibonacci(n-1) + fibonacci(n-2))
        return fibonacciList[n]
    else:
        return fibonacciList[n]


sys.stdout.write(str(fibonacci(int(sys.stdin.readline())))+"\n")
