from heapq import *
import sys
input = sys.stdin.readline
p = sys.stdout.write
n, m = list(map(int, input().split()))
order = sorted([list(map(int, input().split())) for _ in range(m)])
graph = {i: [i-1, i+1] for i in range(2, n)}
graph[1] = [n, 2]
graph[n] = [n-1, 1]
root_end = 1


for k, v in order:
    if k < v:
        continue

    if k == root_end and v == root_end:
        root_end = k
        continue
    elif k == root_end and v != root_end:
        root_end = graph[k][0]
    elif k != root_end and v == root_end:
        root_end = k
    else:
        graph[graph[k][0]][1] = graph[k][1]
        graph[graph[k][1]][0] = graph[k][0]
        graph[graph[v][0]][1] = k
        graph[k][0] = graph[v][0]
        graph[k][1] = v
        graph[v][0] = k

k = root_end
while graph[k][1] != root_end:
    p(str(k)+' ')
    k = graph[k][1]
p(str(k))
