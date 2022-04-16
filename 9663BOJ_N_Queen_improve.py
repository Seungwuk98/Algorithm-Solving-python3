from copy import *
from collections import deque
n = int(input())


def N_queen(x):
    global result
    if x == n:
        result += 1
        return
    for j in range(n):
        row[x] = j

        if available(x):
            N_queen(x+1)


def available(x):
    for i in range(x):
        if row[i] == row[x] or x-i == abs(row[i] - row[x]):
            return False
    return True


result = 0
row = [0]*n
N_queen(0)
print(result)
