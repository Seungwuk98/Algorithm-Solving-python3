a = int(input())
b = list(map(int, input().split()))
d = [0]
for i in b:
    if d[-1] < i:
        d.append(i)
    for j in range(len(d)-1):
        if d[j] < i and d[j+1] > i:
            d[j+1] = i
print(len(d)-1)
