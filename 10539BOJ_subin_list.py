n = int(input())
b = [*map(int, input().split())]
r = []
for i in range(n):
    r.append(b[i]*(i+1)-sum(r))
print(*r)
