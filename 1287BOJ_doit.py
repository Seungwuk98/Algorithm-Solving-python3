s = input()
x = '+-/*('
try:
    for i in range(len(s)):
        if s[i] in x and (not i or s[i-1] in x):
            raise
    print(eval(s))
except:
    print('ROCK')
