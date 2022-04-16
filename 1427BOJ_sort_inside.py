N = int(input())
M = list()
while N != 0:
    M.append(N % 10)
    N = N//10

M.sort()
while M:
    print(M.pop(), end="")
