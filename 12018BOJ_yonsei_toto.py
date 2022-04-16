n, m = map(int, input().split())
mx = []
cnt = 0
for _ in range(n):
    p, l = map(int, input().split())
    lt = [*map(int, input().split())]
    if p < l:
        if m:
            cnt += 1
            m -= 1
        continue
    lt.sort(reverse=True)
    mx.append(lt[l-1])
mx.sort()
for x in mx:
    if m < x:
        break
    cnt += 1
    m -= x
print(cnt)
