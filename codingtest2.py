def solution(n, left, right):
    l_i = left//n
    r_i = right//n
    left -= l_i*n
    right -= l_i*n
    arr = []
    for i in range(l_i, r_i+1):
        arr += [i+1]*(i+1) + [j for j in range(i+2, n+1)]
    return arr[left:right+1]


n = 3
left = 2
right = 5
print(solution(n, left, right))

n = 4
left = 7
right = 14
print(solution(n, left, right))
