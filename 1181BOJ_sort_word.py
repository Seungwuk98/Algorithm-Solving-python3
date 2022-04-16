import sys
input = sys.stdin.readline
n = int(input())
word = [*{input().strip('\n')for _ in range(n)}]
print('\n'.join(sorted(word, key=lambda x: (len(x), x))))
