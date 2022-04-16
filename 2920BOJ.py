arr = [*map(int, input().split())]
x = arr[1]-arr[0]
for i in range(1, 7):
    y = arr[i+1]-arr[i]
    if x*y <= 0:
        print('mixed')
        break
    x = y
else:
    print('ascending' if x > 0 else 'descending')
