import sys
from heapq import *
input = sys.stdin.readline

for _ in range(int(input())):
    min_heap = []
    max_heap = []
    count = {}
    n = int(input())
    _sum = 0
    for __ in range(n):
        o, i = input().split()
        i = int(i)
        if o == 'I':
            heappush(min_heap, i)
            heappush(max_heap, -i)
            if not i in count:
                count[i] = 1
            else:
                count[i] += 1
            _sum += 1
        else:
            if _sum == 0:
                continue
            elif i == 1:
                _max = -heappop(max_heap)
                while not count[_max]:
                    _max = -heappop(max_heap)
                count[_max] -= 1
                _sum -= 1
            else:
                _min = heappop(min_heap)
                while not count[_min]:
                    _min = heappop(min_heap)
                count[_min] -= 1
                _sum -= 1
    if _sum < 1:
        print('EMPTY')
    else:
        _max = -heappop(max_heap)
        while not count[_max]:
            _max = -heappop(max_heap)
        _min = heappop(min_heap)
        while not count[_min]:
            _min = heappop(min_heap)
        print(_max, _min)
