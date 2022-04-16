point_num = int(input())
points = list()
for _ in range(point_num):
    points.append(list(map(int, input().split(' '))))

points.sort()

for i, v in points:
    print(i, v)
