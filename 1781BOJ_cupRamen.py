from collections import deque
import sys
input = sys.stdin.readline
a = int(input())
b = deque(sorted([[*map(int, input().split())]
                  for _ in range(a)], key=lambda x: x[1], reverse=True))

successed = 0
deadline = [False for i in range(0, a+1)]
min_index = 0
for node in b:
    for i in range(node[0], min_index, -1):
        if not deadline[i]:
            deadline[i] = True
            successed += node[1]
            if min_index + 1 == i:
                min_index += 1
            break

print(successed)
