n, m = map(int, input().split())

k = n-m

five = 0
two = 0
c = 5
while n//c:
    five += n//c
    c *= 5
c = 2
while n//c:
    two += n//c
    c *= 2
c = 5
while m//c:
    five -= m//c
    c *= 5
c = 2
while m//c:
    two -= m//c
    c *= 2
c = 5
while k//c:
    five -= k//c
    c *= 5
c = 2
while k//c:
    two -= k//c
    c *= 2

print(min(two, five))
