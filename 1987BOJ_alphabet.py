import sys
input = sys.stdin.readline

r, c = map(int, input().split())
board = []
alphabet = set()
for _ in range(r):
    x = [*input()]
    board.append(x)
    alphabet = alphabet | set(x)
visited_alphabet = [False]*26
max_value = 0
sum_value = 0
d = ((0, 1), (1, 0), (0, -1), (-1, 0))


def dfs(x, y):
    global max_value
    global sum_value
    visit = ord(board[x][y])-65
    visited_alphabet[visit] = True
    sum_value += 1
    nothing = True
    for dx, dy in d:
        if available(x+dx, y+dy):
            nothing = False
            dfs(x+dx, y+dy)
    if nothing and sum_value > max_value:
        max_value = sum_value
    visited_alphabet[visit] = False
    sum_value -= 1
    return


def available(x, y):
    if x >= r or x < 0 or y >= c or y < 0:
        return False
    elif visited_alphabet[ord(board[x][y])-65]:
        return False
    else:
        return True


dfs(0, 0)
print(max_value)
