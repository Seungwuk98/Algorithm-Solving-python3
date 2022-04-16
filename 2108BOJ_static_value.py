import math
n = int(input())
a = sorted([int(input())for _ in range(n)])
mean = math.floor(sum(a)/n+0.5)
print(mean)
medium = a[len(a)//2]
print(medium)
count = dict()
for i in a:
    if i not in count:
        count[i] = 0
    count[i] += 1
max_count = [0, []]
for k, v in count.items():
    if v > max_count[0]:
        max_count = [v, [k]]
    elif v == max_count[0]:
        max_count[1].append(k)
if len(max_count[1]) >= 2:
    max_count[1].sort()
    print(max_count[1][1])
else:
    print(max_count[1][0])
print(a[-1] - a[0])
