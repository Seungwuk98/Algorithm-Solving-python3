from copy import *
n = int(input())


def N_queen(n, i, j, visited):
    # i가 최대가 되면 탈출
    if i == n-1:
        result[0] += 1
    # visited는 카피해서 변환 방지
    tmp = copy(visited)
    tmp.append([i, j])
    # 앞으로 나올 가능성들 모아주기 count
    # i+1, k가 가능한지 확인
    for k in range(n):
        # 모든 visited 들과 비교해서 가능하면 i+1, k로 재귀호출
        for m, l in tmp:
            # print(i+1, k, m, l, available(i+1, k, m, l))
            if not available(i+1, k, m, l):
                break
        else:
            N_queen(n, i+1, k, tmp)


def available(x1, y1, x2, y2):
    if x1 == x2 or y1 == y2 or abs(x2-x1) == abs(y2-y1):
        return False
    else:
        return True


result = [0]
for j in range(n):
    N_queen(n, 0, j, [])

print(result[0])
