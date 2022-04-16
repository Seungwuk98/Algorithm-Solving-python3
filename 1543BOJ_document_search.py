document = input()
search = input()
index = 0
length = len(search)
count = 0

while index < len(document):
    if document[index:index+length] == search:
        count += 1
        index += length
    else:
        index += 1

print(count)
