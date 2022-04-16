s = input()

r = ''
n = ''
for i in s:
    if i == '-':
        r += str(int(n))
        n = ''
        r += ')-('
    elif '0' <= i <= '9':
        n += i
    else:
        r += str(int(n))
        n = ''
        r += i

r = '('+r+str(int(n))+')'
print(eval(r))
