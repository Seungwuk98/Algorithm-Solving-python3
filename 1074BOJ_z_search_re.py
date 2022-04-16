N, row, col = list(map(int, input().split(' ')))


def dfs(N, x, y):
    if N == 0:
        return 0
    N -= 1
    for i in range(2):
        for j in range(2):
            if x < 2**N*(i+1) and y < 2**N*(j+1):
                return (2**(2*N))*(i*2+j)+dfs(N, x-2**N*i, y-2**N*j)


print(dfs(N, row, col))
