def i(): return map(int, input().split())


x1, y1 = i()
x2, y2 = i()
x3, y3 = i()
c = (x2-x1)*(y3-y1)-(x3-x1)*(y2-y1)
print(1 if c > 0 else -1 if c else 0)
