from collections import deque
n = int(input())
k = int(input())
apple = set([tuple(map(int, input().split()))for _ in range(k)])
l = int(input())
turn = dict()
for _ in range(l):
    x, y = input().split()
    turn[int(x)] = y
d = ((0, 1), (1, 0), (0, -1), (-1, 0))
ward, count = 0, 0
snake = deque([(1, 1)])
while True:
    x, y = snake[-1]
    dx, dy = d[ward]
    nx, ny = x+dx, y+dy
    count += 1
    if nx > n or nx < 1 or ny > n or ny < 1 or (nx, ny) in snake:
        break
    snake.append((nx, ny))
    if (nx, ny) in apple:
        apple.remove((nx, ny))
    else:
        snake.popleft()
    if count in turn:
        if turn[count] == 'L':
            ward = (ward-1) % 4
        else:
            ward = (ward+1) % 4
print(count)
