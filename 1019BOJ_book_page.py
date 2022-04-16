n = int(input())


def f(n, d):
    print(d)
    right = 0
    result = 0
    if d:
        i = 1
        while n:
            x = n % 10
            n //= 10
            if d <= x:
                result += n*i+right+1
            else:
                if n-1 >= 0:
                    result += n*i
            right += x*i
            i *= 10
    else:
        i = 1
        while n >= 10:
            x = n % 10
            n //= 10
            if i == 1:
                result += n
            else:
                result += (n-1)*i+right
            right += x*i
            i *= 10
    return result


result = [0]*10
for i in range(10):
    result[i] = f(n, i)
print(*result)
