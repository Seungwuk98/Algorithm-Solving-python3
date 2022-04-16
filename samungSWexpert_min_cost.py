from heapq import *
d = ((1, 0), (-1, 0), (0, 1), (0, -1))

for _ in range(int(input())):
    n = int(input())
    mat = [[*map(int, input().split())]for _ in range(n)]
    distance = [[1e9]*n for _ in range(n)]
    distance[0][0] = 0
    heap = [(0, 0, 0)]
    while heap:
        dist, x, y = heappop(heap)

        for dx, dy in d:
            nx, ny = x+dx, y+dy
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            from_start = dist+1+max(mat[nx][ny]-mat[x][y], 0)
            if distance[nx][ny] > from_start:
                distance[nx][ny] = from_start
                heappush(heap, (from_start, nx, ny))
    print('#'+str(_+1), distance[-1][-1])
