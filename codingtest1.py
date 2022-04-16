def solution(n):
    for i in range(1, 1000000):
        if n % i == 1:
            return i


print(solution(10))
