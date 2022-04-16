from itertools import combinations_with_replacement


def solution(startNumber, endNumber):
    r = startNumber
    answer = [p(str(r))]
    while startNumber % 10 != endNumber:
        if startNumber > endNumber:
            startNumber -= 1
        elif startNumber < endNumber:
            startNumber += 1
        else:
            break
        r = r*10 + startNumber
        answer.append(p(str(r)))
    return answer


def p(n):
    return '0'*(10-len(n))+n


a_comb = combinations_with_replacement(range(10), 2)

for x, y in a_comb:
    print(x, y)
    print(solution(x, y))
    print(y, x)
    print(solution(y, x))
