n = int(input())
w = sorted([*map(int, input().split())])
if 1 not in w:
    print(1)
    exit(0)
for i in range(1, n):
    max_v = sum(w[:i])
    if max_v+1 < w[i]:
        print(max_v+1)
        exit(0)
print(sum(w)+1)
