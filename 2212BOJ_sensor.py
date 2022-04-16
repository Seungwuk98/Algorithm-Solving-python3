from heapq import *

n = int(input())
k = int(input())

if n <= k:
    print(0)
    exit(0)
point = sorted(list(set([*map(int, input().split())])))
edges = []


for i in range(len(point)-1):
    edges.append(point[i+1]-point[i])

edges.sort(reverse=True)

for i in range(k-1):
    edges[i] = 0
print(sum(edges))
