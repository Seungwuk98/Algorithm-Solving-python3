n = int(input())


def sum_j(n):
    sum = 0
    while n != 0:
        sum += n % 10
        n //= 10
    return sum


for i in range(n):
    if i + sum_j(i) == n:
        print(i)
        break
else:
    print(0)
