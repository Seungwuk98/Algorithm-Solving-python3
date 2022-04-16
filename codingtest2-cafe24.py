def solution(a, b):
    _max = len(a)-1
    _min = 0
    c = False
    while _max >= _min:
        mid = (_max+_min)//2
        if a[mid] < b:
            _min = mid+1
        elif a[mid] > b:
            _max = mid-1
        else:
            c = True
            break
    if c:
        return mid
    else:
        return -1


print(solution(1))
