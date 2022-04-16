n = int(input())
chain = [*map(int, input().split())]
chain.sort(reverse=True)

cnt = 0
while chain:
    cnt += chain.pop()
    if len(chain) - 1 <= cnt:
        break
if cnt > len(chain):
    print(len(chain))
else:
    print(cnt)
