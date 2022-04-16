from collections import deque
import sys
input = sys.stdin.readline
n = int(input())

arr = [int(input())for _ in range(n)]
arr.sort()
deq = deque(arr)

cnt = 0
while deq and deq[0] <= 0:
    if len(deq) >= 2 and deq[1] <= 0:
        cnt += deq.popleft() * deq.popleft()
    else:
        cnt += deq.popleft()
        break
while deq and deq[-1] > 1:
    if len(deq) >= 2 and deq[-2] > 1:
        cnt += deq.pop() * deq.pop()
    else:
        cnt += deq.pop()
        break
while deq:
    cnt += deq.pop()

print(cnt)
