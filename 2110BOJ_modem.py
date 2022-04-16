n, m = list(map(int, input().split()))
point = sorted([int(input())for _ in range(n)])
min, max = point[1]-point[0], point[-1]-point[0]
current_gap = 0

while min <= max:
    gap = (min + max)//2
    modem = point[0]
    count = 1
    for i in range(1, len(point)):
        if point[i]-modem >= gap:
            modem = point[i]
            count += 1

    if count >= m:
        min = gap+1
        current_gap = gap
    else:
        max = gap-1

print(current_gap)
