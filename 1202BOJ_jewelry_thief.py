from heapq import *
from collections import deque
import sys
input = sys.stdin.readline
n, k = map(int, input().split())
gems = deque(sorted([[*map(int, input().split())]
                     for _ in range(n)], key=lambda x: x[1], reverse=True))
bags = sorted([int(input())for _ in range(k)])


def insert(m, v, bags, result):
    if m > bags[-1]:
        return result
    _max = len(bags)-1
    _min = 0

    while _max > _min:
        now = (_max+_min)//2

        if m <= bags[now]:
            _max = now
        else:
            _min = now+1

    bags[_max]
    result += v
    return result


result = 0
while bags and gems:
    m, v = gems.popleft()
    result = insert(m, v, bags, result)

print(result)
