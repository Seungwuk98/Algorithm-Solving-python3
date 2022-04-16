n = int(input())
i = 0
min_value = 5000
while 5*i <= n:
    if (n-5*i) % 3 == 0:
        min_value = min(min_value, i+(n-5*i)//3)
    i += 1

if min_value == 5000:
    print(-1)
else:
    print(min_value)
