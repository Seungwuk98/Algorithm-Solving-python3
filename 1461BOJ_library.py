n, m = map(int, input().split())
books = sorted([*map(int, input().split())])
books_left = []
books_right = []
for i in range(n-1):
    if books[i] < 0 and books[i+1] > 0:
        books_left = books[:i+1]
        books_right = books[i+1:]
        break
else:
    if books[0] > 0:
        books_right = books
    elif books[0] < 0:
        books_left = books


result = 0

if books_left and books_right:
    for i in range(0, len(books_left), m):
        result -= books_left[i]*2
    for j in range(len(books_right)-1, -1, (-1)*m):
        result += books_right[j]*2
    if (-1)*books_left[0] >= books_right[-1]:
        result += books_left[0]
    else:
        result -= books_right[-1]
elif books_left:
    for i in range(0, len(books_left), m):
        result -= books_left[i]*2
    result += books_left[0]
elif books_right:
    for j in range(len(books_right)-1, -1, (-1)*m):
        result += books_right[j]*2
    result -= books_right[-1]
print(result)
