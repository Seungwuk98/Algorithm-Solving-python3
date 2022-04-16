n = int(input())
a = [[*map(int, input().split())]for _ in range(n)]


def ccw(x1, y1, x2, y2, x3, y3):
    return (x2-x1)*(y3-y1)-(y2-y1)*(x3-x1)


x1, y1 = a[0]


r = 0
for i in range(2, n):
    x2, y2 = a[i-1]
    x3, y3 = a[i]
    r += ccw(x1, y1, x2, y2, x3, y3)/2
print("%.1f" % (abs(r)))
