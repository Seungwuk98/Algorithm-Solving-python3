N, row, col = list(map(int, input().split(' ')))
searchNum = [0]


def search(N, row, col):
    if N == 0:
        return
    Medium = 2**(N-1)
    if row <= Medium-1 and col <= Medium-1:
        search(N-1, row, col)
    elif row <= Medium-1 and col > Medium-1:
        searchNum[0] += Medium**2
        search(N-1, row, col-Medium)
    elif row > Medium-1 and col <= Medium-1:
        searchNum[0] += Medium**2*2
        search(N-1, row-Medium, col)
    else:
        searchNum[0] += Medium**2*3
        search(N-1, row-Medium, col-Medium)


search(N, row, col)
print(searchNum[0])
