from heapq import *
import sys
input = sys.stdin.readline
n, x = map(int, input().split())
present = [*map(int, input().split())]

K_max = n
K_min = 1


def bisect(k_min, k_max):
    while k_max > k_min:

        k = (k_max+k_min)//2
        lines = [(0, i)for i in range(1, k+1)]
        check = True
        for i in present:
            line, idx = heappop(lines)
            line += i
            if line > x:
                check = False
                break
            heappush(lines, (line, idx))
        if check:
            k_max = k
        else:
            k_min = k+1
    return k_max


print(bisect(K_min, K_max))
