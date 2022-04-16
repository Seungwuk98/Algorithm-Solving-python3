

def solution(n, m, x, y, queries):
    queries.reverse()
    x1, y1, x2, y2 = x, y, x, y
    for q in queries:
        x1, y1, x2, y2 = rq(n, m, x1, y1, x2, y2, q)
        if (x1, y1, x2, y2) == (-1, -1, -1, -1):
            return 0
    return (x2-x1+1)*(y2-y1+1)


def rq(n, m, x1, y1, x2, y2, querie):
    order = querie[0]
    move = querie[1]
    if order == 0:
        if y1 == 0:
            return (x1, y1, x2, min(y2+move, m-1))
        elif y1+move > m-1:
            return (-1, -1, -1, -1)
        else:
            return (x1, y1+move, x2, min(y2+move, m-1))
    elif order == 1:
        if y2 == m-1:
            return (x1, max(0, y1-move), x2, y2)
        elif y2-move < 0:
            return (-1, -1, -1, -1)
        else:
            return (x1, max(0, y1-move), x2, y2-move)
    elif order == 2:
        if x1 == 0:
            return (x1, y1, min(x2+move, n-1), y2)
        elif x1+move > n-1:
            return (-1, -1, -1, -1)
        else:
            return (x1+move, y1, min(x2+move, n-1), y2)
    else:
        if x2 == n-1:
            return (max(x1-move, 0), y1, x2, y2)
        elif x2-move < 0:
            return (-1, -1, -1, -1)
        else:
            return (max(x1-move, 0), y1, x2-move, y2)


n, m, x, y, queries = 2, 2, 0, 0, [[2, 1], [0, 1], [1, 1], [0, 1], [2, 1]]
print(solution(n, m, x, y, queries))

n, m, x, y, queries = 2, 5, 0, 1, [
    [3, 1], [2, 2], [1, 1], [2, 3], [0, 1], [2, 1]]
print(solution(n, m, x, y, queries))

n, m, x, y, queries = 3, 3, 1, 1, [
    [1, 1], [2, 2], [3, 2], [0, 1], [1, 1]]
print(solution(n, m, x, y, queries))
