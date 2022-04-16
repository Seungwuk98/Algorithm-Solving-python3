x, y, w, s = map(int, input().split())
if w*2 < s:
    print(w*(x+y))
else:
    d = s*2
    if x > y:
        x, y = y, x
    cnt = s*x
    y -= x
    if w < s:
        cnt += w*y
    else:
        cnt += y//2 * d + y % 2*w
    print(cnt)
