def chk(s):
    if len(s) <= 1:
        return True
    l = len(s)
    left = s[:l//2]
    right = s[l//2+1:][::-1]
    for i in range(l >> 1):
        if left[i] == right[i]:
            return False
    return chk(left) and chk(right)


for _ in range(int(input())):
    print('YES' if chk(input()) else 'NO')
