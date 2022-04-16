n = input()
l = len(n)
if n == '0':
    print(1)
elif int(n) >= int('1'*l):
    print(l)
else:
    print(l-1)
