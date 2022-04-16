import sys
input = sys.stdin.readline
print = sys.stdout.write


def R(clock, edge, corner):
    if clock:
        corner[2][-1] += 1
        corner[3][-1] -= 1
        corner[7][-1] += 1
        corner[6][-1] -= 1
        corner[2], corner[3], corner[7], corner[6] = corner[6], corner[2], corner[3], corner[7]
        edge[3], edge[7], edge[11], edge[6] = edge[6], edge[3], edge[7], edge[11]
    else:
        corner[2][-1] += 1
        corner[3][-1] -= 1
        corner[7][-1] += 1
        corner[6][-1] -= 1
        corner[2], corner[3], corner[7], corner[6] = corner[3], corner[7],  corner[6], corner[2]
        edge[3], edge[7], edge[11], edge[6] = edge[7], edge[11], edge[6], edge[3]


def L(clock, edge, corner):
    if clock:
        corner[0][-1] += 1
        corner[1][-1] -= 1
        corner[5][-1] += 1
        corner[4][-1] -= 1
        corner[0], corner[1], corner[5], corner[4] = corner[4], corner[0], corner[1], corner[5]
        edge[1], edge[5], edge[9], edge[4] = edge[4], edge[1], edge[5], edge[9]
    else:
        corner[0][-1] += 1
        corner[1][-1] -= 1
        corner[5][-1] += 1
        corner[4][-1] -= 1
        corner[0], corner[1], corner[5], corner[4] = corner[1], corner[5],  corner[4], corner[0]
        edge[1], edge[5], edge[9], edge[4] = edge[5], edge[9], edge[4], edge[1]


def F(clock, edge, corner):
    if clock:
        corner[1][-1] += 1
        corner[2][-1] -= 1
        corner[6][-1] += 1
        corner[5][-1] -= 1
        corner[1], corner[2], corner[6], corner[5] = corner[5], corner[1], corner[2], corner[6]
        edge[2][-1] += 1
        edge[6][-1] -= 1
        edge[10][-1] += 1
        edge[5][-1] -= 1
        edge[2], edge[6], edge[10], edge[5] = edge[5], edge[2], edge[6], edge[10]
    else:
        corner[1][-1] += 1
        corner[2][-1] -= 1
        corner[6][-1] += 1
        corner[5][-1] -= 1
        edge[2][-1] += 1
        edge[6][-1] += 1
        edge[10][-1] += 1
        edge[5][-1] += 1
        corner[1], corner[2], corner[6], corner[5] = corner[2], corner[6], corner[5], corner[1]
        edge[2], edge[6], edge[10], edge[5] = edge[6], edge[10], edge[5], edge[2]


def B(clock, edge, corner):
    if clock:
        corner[3][-1] += 1
        corner[0][-1] -= 1
        corner[4][-1] += 1
        corner[7][-1] -= 1
        corner[0], corner[4], corner[7], corner[3] = corner[3], corner[0], corner[4], corner[7]
        edge[0][-1] += 1
        edge[4][-1] += 1
        edge[8][-1] += 1
        edge[7][-1] += 1
        edge[0], edge[4], edge[8], edge[7] = edge[7], edge[0], edge[4], edge[8]
    else:
        corner[3][-1] += 1
        corner[0][-1] -= 1
        corner[4][-1] += 1
        corner[7][-1] -= 1
        corner[0], corner[4], corner[7], corner[3] = corner[4], corner[7], corner[3], corner[0]
        edge[0][-1] += 1
        edge[4][-1] += 1
        edge[8][-1] += 1
        edge[7][-1] += 1
        edge[0], edge[4], edge[8], edge[7] = edge[4], edge[8], edge[7], edge[0]


def U(clock, edge, corner):
    if clock:
        corner[0], corner[3], corner[2], corner[1] = corner[1], corner[0], corner[3], corner[2]
        edge[0], edge[3], edge[2], edge[1] = edge[1], edge[0], edge[3], edge[2]
    else:
        corner[0], corner[3], corner[2], corner[1] = corner[3], corner[2], corner[1], corner[0]
        edge[0], edge[3], edge[2], edge[1] = edge[3], edge[2], edge[1], edge[0]


def D(clock, edge, corner):
    if clock:
        corner[4], corner[5], corner[6], corner[7] = corner[7], corner[4], corner[5], corner[6]
        edge[8], edge[9], edge[10], edge[11] = edge[11], edge[8], edge[9], edge[10]
    else:
        corner[4], corner[5], corner[6], corner[7] = corner[5], corner[6], corner[7], corner[4]
        edge[8], edge[9], edge[10], edge[11] = edge[9], edge[10], edge[11], edge[8]


corner_color = ['wog', 'wgr', 'wrb', 'wbo', 'ygo', 'yrg', 'ybr', 'yob']
edge_color = ['wo', 'wg', 'wr', 'wb', 'og',
              'rg', 'rb', 'ob', 'yo', 'yg', 'yr', 'yb']

for _ in range(int(input())):
    corner = [[i, 0]for i in range(8)]
    edge = [[i, 0]for i in range(12)]

    n = int(input())
    rotate = [*input().split()]

    for x in rotate:
        if x[-1] == '+':
            clock = True
        else:
            clock = False
        if x[0] == 'F':
            F(clock, edge, corner)
        elif x[0] == 'B':
            B(clock, edge, corner)
        elif x[0] == 'R':
            R(clock, edge, corner)
        elif x[0] == 'L':
            L(clock, edge, corner)
        elif x[0] == 'U':
            U(clock, edge, corner)
        elif x[0] == 'D':
            D(clock, edge, corner)

    count = 0
    result = ''
    for ec, i in [['c', 0], ['e', 0], ['c', 3], ['e', 1], ['t', 0], ['e', 3], ['c', 1], ['e', 2], ['c', 2]]:
        if ec == 'c':
            result += corner_color[corner[i][0]][corner[i][-1] % 3]
        elif ec == 'e':
            result += edge_color[edge[i][0]][edge[i][-1] % 2]
        else:
            result += 'w'
        count += 1
        if count % 3 == 0:
            print(result+'\n')
            result = ''
