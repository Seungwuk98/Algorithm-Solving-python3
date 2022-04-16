from bisect import *
import sys
pnt = sys.stdout.write

d_O=((0,1),(0,2),(0,3),(0,4),(1,0),(1,1),(1,4),(1,5),(2,0),(2,1),
(2,4),(2,5),(3,0),(3,1),(3,4),(3,5),(4,1),(4,2),(4,3),(4,4))
d_N=((0,0),(0,1),(0,4),(0,5),(1,0),(1,1),(1,2),(1,4),(1,5),(2,0),(2,1),
(2,3),(2,4),(2,5),(3,0),(3,1),(3,4),(3,5),(4,0),(4,1),(4,4),(4,5))
d_T=((0,0),(0,1),(0,2),(0,3),(0,4),(0,5),(1,2),
(1,3),(2,2),(2,3),(3,2),(3,3),(4,2),(4,3))
d_A=((0,2),(0,3),(1,1),(1,2),(1,3),(1,4),(2,0),(2,1),(2,4),(2,5),
(3,0),(3,1),(3,2),(3,3),(3,4),(3,5),(4,0),(4,1),(4,4),(4,5))
d_K=((0,0),(0,1),(0,4),(0,5),(1,0),(1,1),(1,3),(1,4),(2,0),(2,1),
(2,2),(2,3),(3,0),(3,1),(3,3),(3,4),(4,0),(4,1),(4,4),(4,5))
d_2=((0,1),(0,2),(0,3),(0,4),(1,0),(1,1),(1,4),(1,5),(2,3),
(2,4),(3,1),(3,2),(4,0),(4,1),(4,2),(4,3),(4,4),(4,5))
d_0=((0,1),(0,2),(0,3),(0,4),(1,0),(1,1),(1,4),(1,5),(2,0),(2,1),
(2,4),(2,5),(3,0),(3,1),(3,4),(3,5),(4,1),(4,2),(4,3),(4,4))
d_1=((0,0),(0,1),(0,2),(1,1),(1,2),
(2,1),(2,2),(3,1),(3,2),(4,1),(4,2))
d_9=((0,1),(0,2),(0,3),(0,4),(1,0),(1,1),(1,4),(1,5),(2,1),
(2,2),(2,3),(2,4),(2,5),(3,4),(3,5),(4,1),(4,2),(4,3),(4,4))
d_com=((3,0),(3,1),(4,1))
d_end=((3,0),(3,1),(4,0),(4,1))
space={0:6,1:3,2:6,',':2}

def al_0(mat, curx, cury):
    for dx, dy in d_0:
        mat[curx+dx][cury+dy] = '#'
    return curx, cury+7


def al_1(mat, curx, cury):
    for dx, dy in d_1:
        mat[curx+dx][cury+dy] = '#'
    return curx, cury+4


def al_2(mat, curx, cury):
    for dx, dy in d_2:
        mat[curx+dx][cury+dy] = '#'
    return curx, cury+7


def al_9(mat, curx, cury):
    for dx, dy in d_9:
        mat[curx+dx][cury+dy] = '#'
    return curx, cury+7


def al_A(mat, curx, cury):
    for dx, dy in d_A:
        mat[curx+dx][cury+dy] = '#'
    return curx, cury+7

def al_K(mat, curx, cury):
    for dx, dy in d_K:
        mat[curx+dx][cury+dy] = '#'
    return curx, cury+7

def al_N(mat, curx, cury):
    for dx, dy in d_N:
        mat[curx+dx][cury+dy] = '#'
    return curx, cury+7


def al_O(mat, curx, cury):
    for dx, dy in d_O:
        mat[curx+dx][cury+dy] = '#'
    return curx, cury+7



def al_T(mat, curx, cury):
    for dx, dy in d_T:
        mat[curx+dx][cury+dy] = '#'
    return curx, cury+6


def al_com(mat, curx, cury):
    for dx, dy in d_com:
        mat[curx+dx][cury+dy] = '#'
    return curx, cury+6


def al_end(mat, curx, cury):
    for dx, dy in d_end:
        mat[curx+dx][cury+dy] = '#'
    return curx, cury+6

al = {'0': al_0, '1': al_1, '2': al_2, '9': al_9, 'A': al_A, ',': al_com, '.': al_end,
      'K': al_K, 'N': al_N, 'O': al_O, 'T' : al_T }

def to3_inv(num):
    ni = []
    while num:
        ni.append(num % 3)
        num //= 3
    return ni


def print_to_shp(mat, curx, cury, num):
    need = 2
    for x in num:
        need += space[x]+1
    if need > 1000-cury:
        curx += 6
        cury = 0
    for x in num:
        curx, cury = al[str(x)](mat, curx, cury)
        if cury >= 1000:
            curx += 6
            cury = 0
    curx, cury = al[','](mat, curx, cury)
    return curx, cury

h_ord = {}
h_ord_inv = {}

for i in range(0, 10):
    h_ord[i] = str(i)
    h_ord_inv[str(i)] = i
    
for i in range(10, 36):
    h_ord[i] = chr(i+55)
    h_ord_inv[chr(i+55)] = i
    
for i in range(36, 62):
    h_ord[i] = chr(i+61)
    h_ord_inv[chr(i+61)] = i
    
def from61(n):
    ret = 0
    c = 1
    for x in n:
        ret += c*h_ord_inv[x]
        c *= 61
    return ret
def to2(x, n):
    ni = [[]for _ in range(n)]
    for i in range(n):
        for j in range(n):
            ni[i].append(x & 1)
            x >>= 1
    return ni

def pr(s, i):
    for j in range(i):
        pnt(s)

s = 'abcdefghijklmnopqrst'

fac = [1]

for i in range(1, 21):
    fac.append(i*fac[-1])

pre = [0]*21
for i in range(1, 21):
    pre[i] += pre[i-1] + fac[i]

def kth(N):
    n = bisect_left(pre, N)
    k = N - pre[n-1]
    cand = [*range(n)]
    result = []
    find(cand, result, k)
    for i in range(n):
        result[i] = s[result[i]]
    return ''.join(result)


def find(cand, result, k):
    if not cand:
        return
    if not k:
        result.append(cand.pop())
    else:
        d, r = divmod(k, fac[len(cand)-1])
        nk = d if r else d-1
        result.append(cand.pop(nk))
        k = r
    find(cand, result, k)
    
def to2_one(x, n):
    ni = []
    for _ in range(n):
        ni.append(x & 1)
        x >>= 1
    return ni

def zero():
    print('ONTAK 2010')

def one():  # clear
    sen = 'Godzilla terrorizes Bajtoly lower again. Every day a monster comes out of the ocean, slow movement of marching through the city to some of the skyscrapers and eats it with people who are in it. Eating one skyscraper takes the whole day, at dusk, it returns to its hiding place hidden in the depths. To make matters worse, going through the city, Godzilla wags its tail and destroys towers, near the passes. The prospect of becoming a meal for an underwater monster, to discourage some residents spent in uncomfort- tion in the city. During the night of each tower is derived as a resident and flees to the countryside. In Bajtogrodzie skyscrapers were built only at street crossings. At each intersection there is exactly one building. Junctions are connected by two-way streets. In addition, a the junction is just above the ocean, this is where Godzilla begins its destructive journey through the city. During the investigation, the monster moves only in the streets. Godzilla noted that he must hurry up with the consumption of residents and carefully choose the skyscrapers devouring and streets, which reaches them. Of course, choosing never previously consumed or destroyed- wanego skyscraper. What is the maximum number of people who can eat before the city completely desolate? Entrance The first line of standard input contains two integers him (1 n 100 000, 0 500 000 m) respectively denoting the number of intersections in the city and the number of connecting streets. Crossroads numbers are numbered from 1 to n, junction 1 is located on the shores of the ocean. Next row contains a sequence of integers n s (0 s 100 000) to describe population skyscrapers at various intersections. In each of the next m rows are the two integers ai and bi (1 ai, bi n, ai = bi), which means that there is a road junction connecting ai and bi. The crossing number One can reach any other intersection in the city. Exit Write to stdout the number of people who eat Godzilla for the optimum choice of meals and roads through the city every day. Example For input: the result is correct: 5 5 11 1 3 2 4 7 1 2 1 3 2 3 2 4 3 5'
    x = 2932
    i = 1
    t = 0
    idx = 0
    while t < 3144693:
        t += x
        pr(sen[idx], x)
        x -= i
        i += 2
        x %= 2932
        if not x:
            x = 2932
        idx += 1


def two():  # clear
    result = [1, 1]
    for _ in range(9999):
        result.append((result[-1]+result[-2]) % 9099099909999099999)
    result[-1] = 0
    print(*result, sep=', ', end='.')


def three():
    result = []

    def sol(arr):
        if len(arr) == 1024:
            return
        n = len(arr)
        narr = ['']*(2*n)
        for i in range(2*n):
            narr[i] = arr[i % n]
        for i in range(n):
            narr[i] += '.'*i
        for i in range(n):
            narr[i] += arr[i]
        sol(narr)
        for i in range(n):
            result.append([*narr[i]])
    sol(['#'])
    result.append(['#'])
    curx, cury = 506, 449
    for x in 'ONTAK':
        curx, cury = al[x](result, curx, cury)
    cury += 3
    for x in '2010':
        curx, cury = al[x](result, curx, cury)
    for x in result:
        print(''.join(x))


def four():
    isprime = [0]*(400002)
    isprime[0] = isprime[1] = 1
    for i in range(int(400002**0.5)+1):
        if not isprime[i]:
            for j in range(i*i, 400002, i):
                isprime[j] = 1
    isprime.pop(0)
    isprime.pop(0)
    x = ''.join(map(str, isprime))
    y = ''
    j = 0
    result = []
    for i in range(len(x)):
        y += x[i]
        j += 1
        if j == 80:
            result.append(y)
            j = 0
            y = ''
    result[3333] = result[3333][:8] + '9099099909999099999' + result[3333][27:]
    for x in result:
        print(x)


def five():
    nd = {1: 'pierwszy', 2: 'drugi', 3: 'trzeci', 4: 'czwarty', 5: 'piaty', 6: 'szosty', 7: 'siodmy', 8: 'osmy', 9: 'dziewiaty', 10: 'dziesiaty', 11: 'jedenasty', 12: 'dwunasty', 13: 'trzynasty', 14: 'czternasty', 15: 'pietnasty', 16: 'szesnasty', 17: 'siedemnasty', 18: 'osiemnasty', 19: 'dziewietnasty', 20: 'dwudziesty', 30: 'trzydziesty', 40: 'czterdziesty', 50: 'piecdziesiaty', 60: 'szescdziesiaty', 70: 'siedemdziesiaty', 80: 'osiemdziesiaty', 90: 'dziewiecdziesiaty', 100: 'setny', '100+': 'sto', 200: 'dwusetny', '200+': 'dwiescie', 300: 'trzysetny', '300+': 'trzysta', '1월': 'stycznia', '2월': 'lutego', '3월': 'marca', '4월': 'kwietnia',
          '5월': 'maja', '6월': 'czerwca', '7월': 'lipca', '8월': 'sierpnia', '9월': 'wrzesnia', '10월': 'pazdziernika', '11월': 'listopada', '12월': 'grudnia', '일': 'dzien', '년도': 'roku', 2000: 'dwutysiecznego', '2*': 'dwa', '1000+': 'tysiace', '1+': 'pierwszego', '2+': 'drugiego', '3+': 'trzeciego', '4+': 'czwartego', '5+': 'piatego', '6+': 'szostego', '7+': 'siodmego', '8+': 'osmego', '9+': 'dziewiatego', '10+': 'dziesiatego', '11+': 'jedenastego', '12+': 'dwunastego', '13+': 'trzynastego', '14+': 'czternastego', '15+': 'pietnastego', '16+': 'szesnastego', '17+': 'siedemnastego', '18+': 'osiemnastego', '19+': 'dziewietnastego', '20+': 'dwudziestego'}

    is_y = {x: False for x in range(2000, 2021)}
    is_y[2000] = is_y[2004] = is_y[2008] = is_y[2012] = is_y[2016] = is_y[2020] = True

    result = []
    mm = [31, [28, 29], 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    for y in range(2000, 2021):
        dday = 0
        if y == 2000:
            yyy = nd[2000]
        else:
            yyy = nd['2*'] + ' ' + nd['1000+'] + ' ' + nd[str(y-2000)+'+']
        for m in range(1, 13):
            if m == 2:
                md = mm[1][+is_y[y]]
            else:
                md = mm[m-1]
            mmm = nd[str(m)+'월']
            for dd in range(1, md+1):
                if dd < 20:
                    dy = nd[dd]
                elif dd % 10:
                    dy = nd[dd//10*10] + ' ' + nd[dd % 10]
                else:
                    dy = nd[dd]
                dday += 1
                if not dday % 100:
                    ddday = nd[dday]
                elif dday < 100:
                    if dday < 20:
                        ddday = nd[dday]
                    elif dday % 10:
                        ddday = nd[dday//10*10] + ' ' + nd[dday % 10]
                    else:
                        ddday = nd[dday]
                else:
                    ddday = nd[str(dday//100*100)+'+']
                    xdday = dday % 100
                    if xdday < 20:
                        ddday += ' ' + nd[xdday]
                    elif xdday % 10:
                        ddday += ' ' + nd[xdday//10*10] + ' ' + nd[xdday % 10]
                    else:
                        ddday += ' ' + nd[xdday]
                ret = '{} {} to {} dzien roku {}.'.format(
                    dy.capitalize(), mmm, ddday, yyy)
                result.append(ret)
    result.append('Koniec.')
    result[2647] = 'Pierwszego kwietnia jest prima aprilis.'
    result[4900] = 'Pierwszego czerwca jest dzien dziecka.'
    for x in result:
        print(x)



def six():
    for i in range(1, 20001):
        t = i**4
        print('T[{}]=\"{}\"'.format(t, kth(t)
              if i != 10000 else "9099099909999099999"))




def seven():
    mat = [['.']*1000 for _ in range(492)]
    cx, cy = 0, 0
    for i in range(171):
        cx, cy = print_to_shp(mat, cx, cy, to3_inv(1 << i))
    cx, cy = al[str(0)](mat, cx, cy)
    cx, cy = al['.'](mat, cx, cy)
    ss1 = '01020102001020021020001020010200120000120001200102010200120120012001200102012001020102012001020102010102010201200120012012001220100200012002010201020102010200'
    ss2 = '120012012001200120012001200120012001200120012012001201002000102001201200020020010020102001200001020102000120002010200102020000102001202002102001200202010201'
    ss3 = '0201020010020201020201020200120010001200201200102012001200120102012002100002010200010200012022020012020102020102020102010909909990999909999902010200120012'
    ss4 = '0012010201020102012001201201020120102012002001020012001200120012000120012001200210200120000120012001201200120102001001001001010100101000020102010200102001020001'
    cx += 7
    cy = 0
    for x in (ss1,ss2,ss3,ss4):
        for y in x:
            cx,cy = al[y](mat,cx,cy)
        cx+=6
        cy=0
    for x in mat:
        print(''.join(x))

def eight():
    sp61 = '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'
    all61 = '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'
    allsp = str(from61(all61))
    sp = to2_one(from61(sp61), 30280)
    all = []
    l = len(allsp)
    i = 0
    for x in sp:
        all.append(int(allsp[i:i+x+1]))
        i += x+1
    d = ((0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1))
    mat = [['.']*1000 for _ in range(1000)]
    x, y = 500, 500
    mat[x][y] = '#'
    for i in range(0, len(all), 2):
        dc = all[i]
        dx, dy = d[dc]
        cnt = all[i+1]
        for i in range(cnt):
            x, y = x + dx, y + dy
            mat[x][y] = '#'
    for x in mat:
        print(''.join(x))

def nine():
    d = ((0, -1), (-1, 0), (-1, 1), (-1, -1))
    def draw(mat, sx, sy, dc, cnt):
        dx, dy = d[dc]
        mat[sx][sy] = '#'
        for i in range(cnt-1):
            sx,sy = sx+dx, sy+dy
            mat[sx][sy] = '#'
    all =[[(125,912,913),(80,933,864),(363,754,755),(992,943,747),(606,895,652),(261,957,602),(753,1002,559),(652,517,518),(157,938,511),(856,825,466),(527,461,462),(576,734,457),(2,986,443),(486,486,437),(994,1002,420),(592,1002,397),(717,591,370),(283,898,347),(325,339,340),(298,1002,333),(124,1002,325),(746,361,324),(466,1002,317),(176,314,315),(167,921,311),(436,584,301),(922,299,300),(64,296,297),(561,353,285),(257,1002,279),(935,649,279),(182,617,271),(619,709,264),(960,845,245),(227,537,236),(55,933,231),(621,640,231),(258,221,222),(526,213,214),(47,1002,213),(421,204,205),(188,576,203),(143,559,198),(917,877,190),(299,182,183),(525,1002,173),(858,465,171),(238,247,164),(369,663,163),(63,1002,149),(832,921,147),(205,903,137),(135,810,131),(698,653,131),(474,387,127),(526,1002,125),(27,504,117),(141,988,117),(324,1002,116),(278,453,109),(384,807,102),(467,94,95),(754,83,84),(473,858,81),(921,1002,69),(362,1002,60),(684,546,59),(468,729,56),(13,535,48),(995,45,46),(268,913,40),(420,1002,37),(593,35,36),(680,29,30),(577,542,29),(175,1002,25),(48,19,20),(651,1002,16),(857,538,16),(513,489,12),(128,460,7),(834,210,7),(99,511,6),(485,813,4),(147,147,3),(169,125,3),(197,97,3),(217,77,3),(269,25,3),(314,199,3),(322,328,3),(332,319,3),(407,892,3),(413,741,3),(419,747,3),(429,757,3),(433,124,3),(453,781,3),(473,958,3),(483,811,3),(486,812,3),(489,26,3),(489,817,3),(502,830,3),(513,841,3),(529,857,3),(531,26,3),(562,957,3),(564,957,3),(617,945,3),(629,957,3),(118,603,2),(119,603,2),(120,840,2),(124,609,2),(129,613,2),(136,856,2),(138,857,2),(151,636,2),(153,637,2),(178,898,2),(180,899,2),(185,670,2),(187,671,2),(189,674,2),(191,675,2),(193,956,2),(195,957,2),(211,696,2),(213,697,2),(232,559,2),(233,559,2),(236,956,2),(237,564,2),(238,957,2),(239,565,2),(241,40,2),(242,40,2),(249,734,2),(251,735,2),(256,25,2),(271,756,2),(273,757,2),(275,760,2),(277,761,2),(287,613,2),(295,780,2),(297,781,2),(300,256,2),(300,349,2),(301,256,2),(302,348,2),(309,247,2),(309,636,2),(311,246,2),(311,637,2),(316,801,2),(317,801,2),(319,237,2),(320,329,2),(321,236,2),(324,326,2),(331,816,2),(333,817,2),(334,315,2),(335,315,2),(339,824,2),(341,825,2),(347,674,2),(349,675,2),(355,840,2),(356,683,2),(357,199,2),(357,683,2),(357,841,2),(359,198,2),(365,192,2),(366,693,2),(367,693,2),(369,696,2),(371,697,2),(371,856,2),(373,857,2),(374,275,2),(376,274,2),(395,722,2),(396,722,2),(406,891,2),(408,892,2),(409,147,2),(411,146,2),(412,237,2),(413,898,2),(414,236,2),(415,899,2),(423,908,2),(424,908,2),(425,224,2),(426,224,2),(431,125,2),(435,122,2),(450,199,2),(452,198,2),(453,103,2),(455,102,2),(456,193,2),(458,192,2),(459,944,2),(461,945,2),(468,181,2),(469,181,2),(471,956,2),(475,959,2),(487,27,2),(491,24,2),(502,147,2),(504,146,2),(504,898,2),(506,899,2),(512,996,2),(517,1002,2),(518,1002,2),(524,125,2),(533,24,2),(539,17,2),(540,17,2),(546,103,2),(548,102,2),(585,865,2),(586,865,2),(624,25,2),(626,24,2),(627,856,2),(629,857,2),(631,18,2),(632,18,2),(666,895,2),(667,895,2),(676,956,2),(678,957,2),(687,967,2),(688,967,2),(727,956,2),(729,957,2),(59,233,1),(60,232,1),(61,231,1),(62,230,1),(66,226,1),(67,225,1),(68,224,1),(69,223,1),(70,222,1),(71,221,1),(72,220,1),(73,219,1),(74,218,1),(75,217,1),(76,216,1),(77,215,1),(78,214,1),(82,210,1),(83,209,1),(84,208,1),(85,207,1),(86,206,1),(87,205,1),(88,204,1),(89,203,1),(90,202,1),(91,201,1),(92,200,1),(93,199,1),(94,198,1),(95,197,1),(96,196,1),(97,195,1),(98,194,1),(99,193,1),(100,192,1),(101,191,1),(102,190,1),(103,189,1),(104,188,1),(105,187,1),(106,186,1),(106,590,1),(107,185,1),(107,591,1),(108,184,1),(108,592,1),(108,827,1),(109,183,1),(109,593,1),(109,828,1),(110,182,1),(110,594,1),(110,829,1),(111,181,1),(111,595,1),(111,830,1),(112,180,1),(112,596,1),(112,831,1),(113,179,1),(113,597,1),(113,832,1),(114,178,1),(114,598,1),(114,833,1),(115,177,1),(115,599,1),(115,834,1),(116,176,1),(116,600,1),(116,835,1),(117,175,1),(117,601,1),(117,836,1),(118,174,1),(118,837,1),(119,173,1),(119,838,1),(120,172,1),(120,604,1),(121,171,1),(121,605,1),(122,170,1),(122,606,1),(123,169,1),(123,607,1),(127,165,1),(127,846,1),(128,164,1),(128,847,1),(129,163,1),(129,848,1),(130,162,1),(130,614,1),(130,849,1),(131,161,1),(131,615,1),(131,850,1),(132,160,1),(132,616,1),(132,851,1),(133,159,1),(133,617,1),(133,852,1),(134,158,1),(134,618,1),(134,853,1),(135,157,1),(135,619,1),(135,854,1),(136,156,1),(136,620,1),(137,155,1),(137,621,1),(138,154,1),(138,622,1),(139,153,1),(139,623,1),(139,858,1),(140,152,1),(140,624,1),(140,859,1),(141,151,1),(141,625,1),(141,860,1),(142,626,1),(142,861,1),(143,627,1),(143,862,1),(144,628,1),(144,863,1),(145,629,1),(145,864,1),(146,630,1),(146,865,1),(147,631,1),(147,866,1),(148,632,1),(148,867,1),(149,633,1),(149,868,1),(150,634,1),(150,869,1),(151,870,1),(152,871,1),(153,872,1),(154,638,1),(154,873,1),(154,916,1),(155,639,1),(155,874,1),(155,917,1),(159,643,1),(159,878,1),(159,921,1),(160,644,1),(160,879,1),(160,922,1),(161,645,1),(161,880,1),(161,923,1),(162,646,1),(162,881,1),(162,924,1),(163,647,1),(163,882,1),(163,925,1),(164,648,1),(164,883,1),(164,926,1),(165,649,1),(165,884,1),(165,927,1),(166,928,1),(167,929,1),(168,930,1),(169,653,1),(169,888,1),(169,931,1),(170,654,1),(170,889,1),(170,932,1),(171,655,1),(171,890,1),(171,933,1),(172,656,1),(172,891,1),(172,934,1),(173,657,1),(173,892,1),(173,935,1),(173,978,1),(174,658,1),(174,893,1),(174,936,1),(175,659,1),(175,894,1),(175,937,1),(176,660,1),(176,895,1),(176,938,1),(177,661,1),(177,896,1),(177,939,1),(177,982,1),(178,662,1),(178,940,1),(178,983,1),(179,663,1),(179,941,1),(179,984,1),(180,664,1),(180,942,1),(180,985,1),(181,665,1),(181,900,1),(181,943,1),(181,986,1),(182,666,1),(182,901,1),(182,944,1),(182,987,1),(183,667,1),(183,902,1),(183,945,1),(183,988,1),(184,668,1),(184,903,1),(184,946,1),(184,989,1),(185,904,1),(185,947,1),(185,990,1),(186,905,1),(186,948,1),(186,991,1),(187,906,1),(187,949,1),(187,992,1),(188,672,1),(188,907,1),(188,950,1),(188,993,1),(189,908,1),(189,951,1),(189,994,1),(190,909,1),(190,952,1),(190,995,1),(191,910,1),(191,953,1),(191,996,1),(192,676,1),(192,911,1),(192,954,1),(192,997,1),(193,677,1),(193,912,1),(193,998,1),(194,678,1),(194,913,1),(194,999,1),(195,679,1),(195,914,1),(195,1000,1),(196,680,1),(196,915,1),(196,958,1),(196,1001,1),(197,681,1),(197,916,1),(197,959,1),(197,1002,1),(198,682,1),(198,917,1),(198,960,1),(199,683,1),(199,918,1),(199,961,1),(200,684,1),(200,919,1),(200,962,1),(201,685,1),(201,920,1),(201,963,1),(202,686,1),(202,921,1),(202,964,1),(203,687,1),(203,922,1),(203,965,1),(204,688,1),(204,923,1),(204,966,1),(205,689,1),(205,924,1),(205,967,1),(206,690,1),(206,925,1),(206,968,1),(207,691,1),(207,926,1),(207,969,1),(208,692,1),(208,927,1),(208,970,1),(209,693,1),(209,928,1),(209,971,1),(210,694,1),(210,929,1),(210,972,1),(211,930,1),(211,973,1),(212,931,1),(212,974,1),(213,932,1),(213,975,1),(214,698,1),(214,933,1),(214,976,1),(215,699,1),(215,934,1),(215,977,1),(216,700,1),(216,935,1),(216,978,1),(217,701,1),(217,936,1),(217,979,1),(218,702,1),(218,937,1),(218,980,1),(219,938,1),(219,981,1),(220,704,1),(220,939,1),(220,982,1),(221,705,1),(221,940,1),(221,983,1),(222,706,1),(222,941,1),(222,984,1),(223,942,1),(223,985,1),(224,708,1),(224,943,1),(224,986,1),(225,709,1),(225,944,1),(225,987,1),(226,55,1),(226,710,1),(226,945,1),(226,988,1),(227,54,1),(227,711,1),(227,946,1),(227,989,1),(228,53,1),(228,712,1),(228,947,1),(228,990,1),(229,52,1),(229,713,1),(229,948,1),(229,991,1),(230,51,1),(230,556,1),(230,714,1),(230,949,1),(230,992,1),(231,50,1),(231,557,1),(231,715,1),(231,950,1),(231,993,1),(232,49,1),(232,716,1),(232,951,1),(232,994,1),(233,48,1),(233,717,1),(233,952,1),(233,995,1),(234,47,1),(234,560,1),(234,718,1),(234,953,1),(234,996,1),(235,46,1),(235,561,1),(235,719,1),(235,954,1),(235,997,1),(236,45,1),(236,562,1),(236,720,1),(236,998,1),(237,44,1),(237,412,1),(237,721,1),(237,999,1),(238,43,1),(238,411,1),(238,722,1),(238,1000,1),(239,42,1),(239,410,1),(239,723,1),(239,958,1),(239,1001,1),(240,41,1),(240,409,1),(240,566,1),(240,724,1),(240,959,1),(240,1002,1),(241,408,1),(241,567,1),(241,725,1),(241,960,1),(242,407,1),(242,568,1),(242,726,1),(242,961,1),(243,38,1),(243,406,1),(243,569,1),(243,727,1),(243,962,1),(244,37,1),(244,405,1),(244,570,1),(244,728,1),(244,963,1),(245,36,1),(245,404,1),(245,571,1),(245,729,1),(245,964,1),(246,35,1),(246,403,1),(246,572,1),(246,730,1),(246,965,1),(247,34,1),(247,402,1),(247,573,1),(247,731,1),(247,966,1),(248,33,1),(248,401,1),(248,574,1),(248,732,1),(248,967,1),(249,32,1),(249,400,1),(249,575,1),(249,968,1),(250,31,1),(250,399,1),(250,576,1),(250,969,1),(251,30,1),(251,398,1),(251,577,1),(251,970,1),(252,29,1),(252,397,1),(252,578,1),(252,736,1),(252,971,1),(253,28,1),(253,303,1),(253,396,1),(253,579,1),(253,737,1),(253,972,1),(254,27,1),(254,302,1),(254,395,1),(254,580,1),(254,738,1),(254,973,1),(255,26,1),(255,301,1),(255,394,1),(255,581,1),(255,739,1),(255,974,1),(256,300,1),(256,393,1),(256,582,1),(257,299,1),(257,392,1),(257,583,1),(258,298,1),(258,391,1),(258,584,1),(259,297,1),(259,390,1),(259,585,1),(259,743,1),(259,978,1),(260,21,1),(260,296,1),(260,979,1),(261,20,1),(261,295,1),(261,980,1),(262,19,1),(262,294,1),(262,981,1),(263,293,1),(263,386,1),(263,589,1),(263,747,1),(263,982,1),(264,17,1),(264,292,1),(264,385,1),(264,590,1),(264,748,1),(264,983,1),(265,16,1),(265,291,1),(265,384,1),(265,591,1),(265,749,1),(265,984,1),(266,15,1),(266,290,1),(266,383,1),(266,592,1),(266,750,1),(266,985,1),(267,14,1),(267,289,1),(267,382,1),(267,593,1),(267,751,1),(267,986,1),(268,13,1),(268,288,1),(268,381,1),(268,594,1),(268,752,1),(268,987,1),(269,12,1),(269,287,1),(269,380,1),(269,595,1),(269,753,1),(269,988,1),(270,11,1),(270,286,1),(270,379,1),(270,596,1),(270,754,1),(270,989,1),(271,10,1),(271,285,1),(271,378,1),(271,597,1),(271,990,1),(272,9,1),(272,284,1),(272,377,1),(272,598,1),(272,991,1),(273,8,1),(273,283,1),(273,376,1),(273,599,1),(273,992,1),(274,7,1),(274,282,1),(274,375,1),(274,600,1),(274,758,1),(274,993,1),(275,6,1),(275,281,1),(275,374,1),(275,601,1),(275,994,1),(276,5,1),(276,280,1),(276,373,1),(276,602,1),(276,995,1),(277,4,1),(277,279,1),(277,603,1),(277,996,1),(278,3,1),(278,278,1),(278,604,1),(278,762,1),(278,997,1),(279,2,1),(279,277,1),(279,605,1),(279,763,1),(279,998,1),(280,1,1),(280,369,1),(280,606,1),(280,764,1),(280,999,1),(281,0,1),(281,275,1),(281,368,1),(281,607,1),(281,765,1),(281,1000,1),(282,274,1),(282,367,1),(282,1001,1),(283,273,1),(283,366,1),(284,272,1),(284,365,1),(285,364,1),(285,769,1),(285,1001,1),(286,270,1),(286,363,1),(286,770,1),(286,1000,1),(287,269,1),(287,362,1),(287,771,1),(288,361,1),(288,614,1),(288,772,1),(289,267,1),(289,360,1),(289,615,1),(289,773,1),(290,266,1),(290,359,1),(290,616,1),(290,774,1),(291,265,1),(291,358,1),(291,617,1),(291,775,1),(292,264,1),(292,357,1),(292,618,1),(292,776,1),(293,263,1),(293,356,1),(293,619,1),(293,777,1),(294,0,1),(294,262,1),(294,355,1),(294,620,1),(294,778,1),(295,261,1),(295,354,1),(295,621,1),(295,1002,1),(296,260,1),(296,353,1),(296,622,1),(296,1001,1),(297,259,1),(297,352,1),(297,623,1),(298,258,1),(298,351,1),(299,257,1),(299,350,1),(299,625,1),(300,626,1),(300,784,1),(301,627,1),(301,785,1),(302,254,1),(302,628,1),(302,786,1),(303,253,1),(303,346,1),(303,629,1),(303,787,1),(304,252,1),(304,345,1),(304,630,1),(304,788,1),(305,251,1),(305,344,1),(305,631,1),(305,789,1),(306,250,1),(306,632,1),(306,790,1),(307,249,1),(307,342,1),(307,633,1),(307,791,1),(308,248,1),(308,341,1),(308,634,1),(308,792,1),(309,340,1),(309,793,1),(310,339,1),(310,794,1),(311,338,1),(311,795,1),(312,244,1),(312,337,1),(312,638,1),(312,796,1),(313,243,1),(313,336,1),(313,639,1),(313,797,1),(314,242,1),(314,335,1),(314,640,1),(315,241,1),(315,334,1),(315,641,1),(315,799,1),(316,240,1),(316,333,1),(316,642,1),(317,239,1),(317,332,1),(317,643,1),(318,238,1),(318,331,1),(318,644,1),(318,802,1),(319,330,1),(319,645,1),(319,803,1),(320,646,1),(320,804,1),(321,647,1),(321,805,1),(322,234,1),(322,648,1),(322,806,1),(323,233,1),(323,649,1),(323,807,1),(324,650,1),(324,808,1),(325,651,1),(325,809,1),(326,652,1),(326,810,1),(327,229,1),(327,653,1),(327,811,1),(328,228,1),(328,321,1),(328,654,1),(329,227,1),(329,320,1),(329,655,1),(329,813,1),(330,226,1),(330,319,1),(330,656,1),(330,814,1),(331,225,1),(331,657,1),(332,224,1),(332,658,1),(333,223,1),(333,316,1),(333,659,1),(334,222,1),(334,660,1),(334,818,1),(335,221,1),(335,661,1),(335,819,1),(336,220,1),(336,313,1),(336,662,1),(336,820,1),(337,219,1),(337,312,1),(337,663,1),(337,821,1),(338,218,1),(338,311,1),(338,822,1),(339,217,1),(339,310,1),(339,665,1),(340,216,1),(340,309,1),(340,666,1),(341,215,1),(341,308,1),(341,667,1),(342,214,1),(342,307,1),(342,668,1),(342,826,1),(343,213,1),(343,306,1),(343,669,1),(343,827,1),(344,212,1),(344,305,1),(344,670,1),(344,828,1),(345,211,1),(345,304,1),(345,671,1),(345,829,1),(346,210,1),(346,303,1),(346,672,1),(346,830,1),(347,209,1),(347,831,1),(348,208,1),(348,301,1),(348,832,1),(349,207,1),(349,300,1),(349,833,1),(350,206,1),(350,299,1),(350,676,1),(350,834,1),(351,205,1),(351,298,1),(351,677,1),(351,835,1),(352,204,1),(352,297,1),(352,678,1),(352,836,1),(353,203,1),(353,296,1),(353,679,1),(353,837,1),(354,202,1),(354,295,1),(354,680,1),(354,838,1),(355,201,1),(355,294,1),(355,681,1),(356,200,1),(356,293,1),(357,292,1),(358,291,1),(358,684,1),(358,842,1),(359,290,1),(359,685,1),(359,843,1),(360,196,1),(360,289,1),(360,686,1),(360,844,1),(361,195,1),(361,288,1),(361,687,1),(361,845,1),(362,846,1),(363,847,1),(364,848,1),(365,284,1),(365,691,1),(365,849,1),(366,190,1),(366,283,1),(366,850,1),(367,189,1),(367,282,1),(367,851,1),(368,188,1),(368,281,1),(368,694,1),(368,852,1),(369,187,1),(369,280,1),(369,853,1),(370,186,1),(370,279,1),(371,185,1),(371,278,1),(372,184,1),(372,277,1),(372,698,1),(373,183,1),(373,276,1),(373,699,1),(374,182,1),(374,700,1),(374,858,1),(375,181,1),(375,701,1),(375,859,1),(376,180,1),(376,702,1),(376,860,1),(377,179,1),(377,272,1),(377,703,1),(377,861,1),(378,178,1),(378,271,1),(378,704,1),(378,862,1),(379,270,1),(379,705,1),(379,863,1),(380,176,1),(380,269,1),(380,706,1),(380,864,1),(381,175,1),(381,268,1),(381,707,1),(381,865,1),(382,174,1),(382,267,1),(382,708,1),(382,866,1),(383,173,1),(383,266,1),(383,867,1),(384,172,1),(384,265,1),(384,868,1),(385,171,1),(385,264,1),(385,869,1),(386,170,1),(386,263,1),(386,712,1),(386,870,1),(387,169,1),(387,262,1),(387,713,1),(387,871,1),(388,168,1),(388,261,1),(388,714,1),(388,872,1),(389,167,1),(389,260,1),(389,715,1),(389,873,1),(390,166,1),(390,259,1),(390,716,1),(390,874,1),(391,165,1),(391,258,1),(391,717,1),(391,875,1),(392,164,1),(392,257,1),(392,718,1),(392,876,1),(393,163,1),(393,256,1),(393,877,1),(394,162,1),(394,255,1),(394,720,1),(394,878,1),(395,161,1),(395,254,1),(395,879,1),(396,160,1),(396,253,1),(396,880,1),(397,159,1),(397,252,1),(397,881,1),(398,158,1),(398,251,1),(398,882,1),(399,157,1),(399,250,1),(399,883,1),(400,156,1),(400,249,1),(400,884,1),(401,155,1),(401,248,1),(402,154,1),(402,247,1),(402,886,1),(403,153,1),(403,246,1),(403,887,1),(404,152,1),(404,245,1),(404,888,1),(405,151,1),(405,244,1),(405,889,1),(406,150,1),(406,243,1),(407,149,1),(407,242,1),(408,148,1),(408,241,1),(409,240,1),(409,893,1),(410,239,1),(410,894,1),(411,238,1),(411,895,1),(412,144,1),(412,896,1),(413,143,1),(414,142,1),(415,99,1),(415,141,1),(415,234,1),(416,98,1),(416,140,1),(416,233,1),(416,900,1),(417,97,1),(417,139,1),(417,232,1),(417,901,1),(418,96,1),(418,138,1),(418,231,1),(418,902,1),(419,95,1),(419,137,1),(419,230,1),(419,903,1),(420,229,1),(420,904,1),(421,228,1),(421,905,1),(422,227,1),(422,906,1),(423,91,1),(423,133,1),(423,226,1),(424,90,1),(424,132,1),(424,225,1),(425,89,1),(425,131,1),(425,909,1),(426,88,1),(426,130,1),(426,910,1),(427,87,1),(427,129,1),(427,222,1),(427,911,1),(428,86,1),(428,128,1),(428,221,1),(428,912,1),(429,85,1),(429,127,1),(429,220,1),(429,913,1),(430,84,1),(430,126,1),(430,219,1),(430,914,1),(431,83,1),(431,218,1),(431,915,1),(432,82,1),(432,217,1),(432,916,1),(433,81,1),(433,216,1),(433,917,1),(434,80,1),(434,215,1),(434,918,1),(435,79,1),(435,919,1),(436,78,1),(436,120,1),(436,213,1),(436,920,1),(437,77,1),(437,119,1),(437,212,1),(437,921,1),(438,76,1),(438,118,1),(438,211,1),(438,922,1),(439,75,1),(439,117,1),(439,210,1),(439,923,1),(440,74,1),(440,116,1),(440,209,1),(440,924,1),(441,73,1),(441,115,1),(441,208,1),(441,925,1),(442,72,1),(442,114,1),(442,207,1),(442,926,1),(443,71,1),(443,113,1),(443,206,1),(443,927,1),(444,70,1),(444,112,1),(444,205,1),(444,928,1),(445,69,1),(445,111,1),(445,204,1),(445,929,1),(446,68,1),(446,110,1),(446,203,1),(446,930,1),(447,67,1),(447,109,1),(447,202,1),(447,931,1),(448,66,1),(448,108,1),(448,201,1),(448,932,1),(449,65,1),(449,107,1),(449,200,1),(449,933,1),(450,64,1),(450,106,1),(450,934,1),(451,63,1),(451,105,1),(451,935,1),(452,62,1),(452,104,1),(452,936,1),(453,61,1),(453,196,1),(453,937,1),(454,60,1),(454,195,1),(454,938,1),(455,59,1),(455,194,1),(455,939,1),(456,58,1),(456,100,1),(456,940,1),(457,57,1),(457,99,1),(457,941,1),(458,56,1),(458,98,1),(458,942,1),(459,55,1),(459,97,1),(459,190,1),(460,54,1),(460,96,1),(460,189,1),(461,53,1),(461,95,1),(461,188,1),(462,52,1),(462,94,1),(462,187,1),(462,946,1),(463,51,1),(463,93,1),(463,186,1),(463,947,1),(464,50,1),(464,92,1),(464,185,1),(464,948,1),(465,49,1),(465,91,1),(465,184,1),(466,183,1),(467,182,1),(468,952,1),(469,45,1),(469,87,1),(469,953,1),(470,44,1),(470,86,1),(470,179,1),(470,954,1),(471,43,1),(471,85,1),(471,178,1),(472,42,1),(472,84,1),(472,177,1),(473,41,1),(473,83,1),(473,176,1),(474,40,1),(474,82,1),(474,175,1),(474,867,1),(475,39,1),(475,81,1),(475,174,1),(475,868,1),(476,38,1),(476,80,1),(476,173,1),(476,869,1),(476,960,1),(477,37,1),(477,79,1),(477,172,1),(477,870,1),(477,961,1),(478,36,1),(478,78,1),(478,171,1),(478,871,1),(478,962,1),(479,35,1),(479,77,1),(479,170,1),(479,872,1),(479,963,1),(480,34,1),(480,76,1),(480,169,1),(480,873,1),(480,964,1),(481,33,1),(481,75,1),(481,168,1),(481,874,1),(481,965,1),(482,32,1),(482,74,1),(482,167,1),(482,875,1),(482,966,1),(483,31,1),(483,73,1),(483,166,1),(483,876,1),(483,967,1),(484,30,1),(484,72,1),(484,165,1),(484,877,1),(484,968,1),(485,29,1),(485,878,1),(485,969,1),(486,28,1),(486,879,1),(486,970,1),(487,880,1),(487,971,1),(488,68,1),(488,161,1),(488,881,1),(488,972,1),(489,67,1),(489,160,1),(489,882,1),(489,973,1),(490,66,1),(490,159,1),(490,883,1),(490,974,1),(491,65,1),(491,158,1),(491,884,1),(491,975,1),(492,22,1),(492,64,1),(492,157,1),(492,885,1),(492,976,1),(493,21,1),(493,63,1),(493,156,1),(493,886,1),(493,977,1),(494,20,1),(494,62,1),(494,155,1),(494,887,1),(494,978,1),(495,19,1),(495,61,1),(495,154,1),(495,888,1),(495,979,1),(496,18,1),(496,60,1),(496,153,1),(496,889,1),(496,980,1),(497,17,1),(497,59,1),(497,152,1),(497,890,1),(497,981,1),(498,16,1),(498,58,1),(498,151,1),(498,891,1),(498,982,1),(499,15,1),(499,57,1),(499,150,1),(499,892,1),(499,983,1),(500,14,1),(500,56,1),(500,149,1),(500,893,1),(500,984,1),(501,13,1),(501,55,1),(501,148,1),(501,894,1),(501,985,1),(502,12,1),(502,54,1),(502,895,1),(502,986,1),(503,11,1),(503,53,1),(503,896,1),(503,987,1),(504,10,1),(504,52,1),(504,988,1),(505,9,1),(505,51,1),(505,144,1),(505,989,1),(506,8,1),(506,50,1),(506,143,1),(506,990,1),(507,7,1),(507,49,1),(507,142,1),(507,900,1),(507,991,1),(508,6,1),(508,48,1),(508,141,1),(508,901,1),(508,992,1),(509,5,1),(509,47,1),(509,140,1),(509,902,1),(509,993,1),(510,4,1),(510,46,1),(510,139,1),(510,903,1),(510,994,1),(511,3,1),(511,45,1),(511,138,1),(511,904,1),(512,2,1),(512,44,1),(512,137,1),(512,905,1),(513,1,1),(513,43,1),(513,136,1),(513,906,1),(513,997,1),(514,0,1),(514,42,1),(514,135,1),(514,907,1),(514,998,1),(515,41,1),(515,134,1),(515,908,1),(515,999,1),(516,40,1),(516,133,1),(516,909,1),(516,1000,1),(517,39,1),(517,132,1),(517,910,1),(518,38,1),(518,131,1),(518,911,1),(519,37,1),(519,130,1),(519,912,1),(519,1000,1),(520,36,1),(520,129,1),(520,913,1),(521,35,1),(521,128,1),(521,914,1),(522,34,1),(522,127,1),(522,915,1),(523,33,1),(523,126,1),(523,916,1),(524,32,1),(528,921,1),(529,120,1),(529,922,1),(530,119,1),(530,923,1),(531,118,1),(531,924,1),(532,117,1),(532,925,1),(533,116,1),(533,926,1),(534,22,1),(534,115,1),(534,927,1),(535,21,1),(535,114,1),(535,928,1),(536,20,1),(536,113,1),(536,929,1),(537,19,1),(537,112,1),(537,930,1),(538,18,1),(538,111,1),(538,931,1),(539,110,1),(539,932,1),(540,109,1),(540,933,1),(541,15,1),(541,108,1),(541,934,1),(542,14,1),(542,107,1),(542,935,1),(543,13,1),(543,106,1),(543,936,1),(544,12,1),(544,105,1),(544,937,1),(545,11,1),(545,104,1),(545,938,1),(546,10,1),(546,939,1),(547,9,1),(547,940,1),(548,8,1),(548,941,1),(549,7,1),(549,100,1),(549,942,1),(550,6,1),(550,99,1),(550,943,1),(551,5,1),(551,98,1),(551,944,1),(552,4,1),(552,97,1),(552,945,1),(553,3,1),(553,96,1),(553,946,1),(554,2,1),(554,95,1),(554,947,1),(555,1,1),(555,94,1),(555,948,1),(556,0,1),(556,93,1),(556,949,1),(557,92,1),(558,91,1),(558,951,1),(559,90,1),(559,952,1),(559,1002,1),(560,953,1),(560,1001,1),(561,954,1),(561,1000,1),(563,86,1),(564,85,1),(565,84,1),(565,958,1),(566,83,1),(566,959,1),(567,82,1),(567,960,1),(568,81,1),(568,961,1),(569,80,1),(569,962,1),(570,79,1),(570,963,1),(571,78,1),(571,964,1),(572,77,1),(572,965,1),(573,76,1),(573,966,1),(574,75,1),(574,967,1),(575,74,1),(575,968,1),(576,73,1),(576,969,1),(577,72,1),(577,970,1),(578,71,1),(578,971,1),(579,70,1),(579,858,1),(579,972,1),(580,69,1),(580,859,1),(580,973,1),(581,68,1),(581,860,1),(581,974,1),(582,67,1),(582,861,1),(582,975,1),(583,66,1),(583,862,1),(583,976,1),(584,65,1),(584,863,1),(585,64,1),(585,978,1),(586,979,1),(587,62,1),(587,866,1),(587,980,1),(588,61,1),(588,867,1),(588,981,1),(589,60,1),(589,868,1),(589,982,1),(590,59,1),(590,869,1),(590,983,1),(591,58,1),(592,57,1),(593,56,1),(594,873,1),(594,987,1),(595,54,1),(595,874,1),(595,988,1),(596,53,1),(596,875,1),(596,989,1),(597,52,1),(597,876,1),(597,990,1),(598,51,1),(598,877,1),(598,991,1),(599,50,1),(599,878,1),(599,992,1),(600,49,1),(600,879,1),(600,993,1),(601,48,1),(601,880,1),(601,994,1),(602,47,1),(602,881,1),(602,995,1),(603,46,1),(603,882,1),(603,996,1),(604,45,1),(604,883,1),(604,997,1),(605,44,1),(605,998,1),(606,43,1),(606,999,1),(607,42,1),(607,1000,1),(608,41,1),(608,887,1),(608,1001,1),(609,40,1),(609,888,1),(609,1002,1),(610,39,1),(610,889,1),(611,38,1),(611,890,1),(612,37,1),(612,891,1),(613,36,1),(613,892,1),(614,35,1),(614,893,1),(615,34,1),(615,894,1),(616,33,1),(616,895,1),(617,32,1),(617,896,1),(618,31,1),(618,897,1),(619,30,1),(619,898,1),(620,29,1),(620,899,1),(621,28,1),(621,900,1),(622,27,1),(622,901,1),(623,26,1),(623,902,1),(624,852,1),(624,903,1),(625,853,1),(625,904,1),(626,854,1),(626,905,1),(627,22,1),(627,906,1),(628,21,1),(628,907,1),(629,20,1),(629,908,1),(630,19,1),(630,858,1),(630,909,1),(631,859,1),(631,910,1),(632,860,1),(632,911,1),(633,16,1),(633,861,1),(633,912,1),(634,15,1),(634,862,1),(634,913,1),(635,14,1),(635,863,1),(635,914,1),(636,13,1),(636,864,1),(636,915,1),(637,12,1),(637,865,1),(637,916,1),(638,11,1),(638,866,1),(638,917,1),(639,10,1),(639,867,1),(639,918,1),(640,9,1),(640,868,1),(640,919,1),(641,8,1),(641,869,1),(642,7,1),(642,870,1),(642,921,1),(643,6,1),(643,871,1),(643,922,1),(644,5,1),(644,872,1),(644,923,1),(645,4,1),(645,873,1),(645,924,1),(646,3,1),(646,874,1),(646,925,1),(647,2,1),(647,875,1),(647,926,1),(648,1,1),(648,876,1),(648,927,1),(649,0,1),(649,877,1),(649,928,1),(650,878,1),(650,929,1),(651,879,1),(651,930,1),(652,880,1),(652,931,1),(653,881,1),(653,932,1),(653,1001,1),(654,882,1),(654,933,1),(654,1000,1),(655,883,1),(655,934,1),(656,884,1),(656,935,1),(657,885,1),(657,936,1),(658,886,1),(658,937,1),(659,887,1),(659,938,1),(660,888,1),(660,939,1),(661,889,1),(661,940,1),(662,890,1),(662,941,1),(663,891,1),(663,942,1),(664,892,1),(664,943,1),(665,893,1),(665,944,1),(666,945,1),(667,946,1),(668,896,1),(668,947,1),(669,897,1),(669,948,1),(670,898,1),(670,949,1),(671,899,1),(671,950,1),(672,900,1),(672,951,1),(672,1000,1),(673,901,1),(673,952,1),(673,999,1),(673,1001,1),(674,902,1),(674,953,1),(674,1000,1),(674,1002,1),(675,903,1),(675,954,1),(675,1001,1),(676,904,1),(676,1002,1),(677,905,1),(678,906,1),(679,907,1),(679,958,1),(680,908,1),(680,959,1),(681,909,1),(681,960,1),(682,910,1),(682,961,1),(683,911,1),(683,962,1),(684,912,1),(684,963,1),(685,913,1),(685,964,1),(686,914,1),(686,965,1),(687,915,1),(688,916,1),(689,917,1),(689,968,1),(690,918,1),(690,969,1),(691,919,1),(691,970,1),(692,920,1),(692,971,1),(693,921,1),(693,972,1),(694,922,1),(694,973,1),(695,923,1),(695,974,1),(696,924,1),(696,975,1),(697,925,1),(697,976,1),(698,926,1),(698,977,1),(699,927,1),(699,978,1),(700,928,1),(700,979,1),(701,929,1),(701,980,1),(702,930,1),(702,981,1),(703,931,1),(703,982,1),(704,932,1),(704,983,1),(705,933,1),(705,984,1),(706,934,1),(706,985,1),(707,935,1),(707,986,1),(708,936,1),(708,987,1),(709,937,1),(709,988,1),(710,938,1),(710,989,1),(711,939,1),(711,990,1),(712,940,1),(712,991,1),(713,992,1),(714,942,1),(714,993,1),(715,943,1),(715,994,1),(716,944,1),(716,995,1),(717,945,1),(717,996,1),(718,946,1),(718,997,1),(719,947,1),(719,998,1),(720,948,1),(720,999,1),(721,949,1),(721,1000,1),(722,950,1),(722,1001,1),(723,951,1),(723,1002,1),(724,952,1),(725,953,1),(726,954,1),(730,958,1),(731,959,1),(732,960,1),(733,961,1),(734,962,1),(735,963,1),(736,964,1),(737,965,1),(738,966,1),(739,967,1),(740,968,1),(741,969,1),(742,970,1),(743,971,1),(744,972,1),(745,973,1),(746,974,1),(747,975,1),(748,976,1),(749,977,1),(750,978,1),(751,979,1),(755,983,1),(756,984,1),(757,985,1),(758,986,1),(759,987,1),(760,988,1),(761,989,1),(762,990,1),(763,991,1),(764,992,1),(765,993,1),(766,994,1),(767,995,1),(768,996,1),(769,997,1),(770,998,1),(771,999,1),(772,1000,1),(773,1001,1),(774,1002,1),(782,980,1),(783,981,1),(784,982,1),(785,983,1),(786,984,1),(787,985,1),(788,986,1),(789,987,1),(790,988,1),(791,989,1),(792,990,1),(794,992,1),(795,993,1),(796,994,1),(797,995,1),(798,996,1),(799,997,1),(800,998,1),(801,999,1),(802,1000,1),(803,1001,1),(804,1002,1)],[(889,636,875),(868,146,845),(908,612,818),(970,122,791),(785,506,764),(970,564,764),(937,956,759),(815,428,751),(799,856,723),(836,484,708),(769,674,658),(909,454,627),(946,450,622),(650,840,612),(871,274,570),(907,810,563),(877,332,557),(744,24,550),(795,570,514),(588,124,506),(650,816,502),(694,236,487),(983,538,466),(763,102,457),(860,604,438),(585,198,428),(643,780,426),(539,898,419),(948,474,397),(696,326,385),(947,618,372),(886,166,368),(371,76,330),(578,756,323),(371,824,303),(478,696,302),(522,348,294),(344,246,279),(926,266,273),(426,328,264),(398,734,264),(878,832,259),(772,376,229),(630,632,225),(245,296,208),(629,800,203),(891,764,196),(587,746,188),(483,192,187),(766,606,183),(561,26,177),(236,96,175),(194,408,153),(972,898,141),(886,552,136),(226,736,124),(493,314,118),(201,670,93),(821,180,67),(110,258,65),(115,398,62),(320,760,57),(526,958,57),(481,944,48),(149,202,44),(132,396,43),(836,990,43),(748,610,39),(620,860,34),(606,964,33),(381,586,23),(975,524,19),(710,402,13),(528,28,3),(527,31,3),(259,35,3),(177,117,3),(327,322,3),(327,323,3),(414,740,3),(467,793,3),(486,812,3),(503,829,3),(125,842,3),(126,845,3),(526,852,3),(526,917,3),(593,919,3),(527,920,3),(618,944,3),(299,1000,3),(259,22,2),(468,46,2),(467,48,2),(487,69,2),(486,71,2),(562,87,2),(468,88,2),(561,89,2),(467,90,2),(422,92,2),(421,94,2),(421,136,2),(487,162,2),(486,164,2),(126,166,2),(125,168,2),(363,194,2),(81,211,2),(80,213,2),(65,227,2),(64,229,2),(326,230,2),(325,232,2),(364,285,2),(363,287,2),(279,370,2),(278,372,2),(262,387,2),(261,389,2),(261,586,2),(262,588,2),(283,608,2),(157,640,2),(158,642,2),(167,650,2),(168,652,2),(363,688,2),(364,690,2),(384,709,2),(385,711,2),(257,740,2),(258,742,2),(261,744,2),(262,746,2),(283,766,2),(284,768,2),(299,783,2),(592,870,2),(593,872,2),(157,875,2),(158,877,2),(606,884,2),(167,885,2),(607,886,2),(168,887,2),(157,918,2),(158,920,2),(466,949,2),(467,951,2),(257,975,2),(258,977,2),(175,979,2),(753,980,2),(176,981,2),(754,982,2),(592,984,2),(593,986,2),(512,995,2),(284,1002,2),(298,1002,2),(652,1002,2)],[(875,265,585),(874,165,551),(578,344,529),(826,382,459),(840,491,451),(753,231,341),(752,174,333),(748,321,323),(566,658,307),(503,288,305),(361,360,298),(865,585,297),(578,708,292),(702,120,265),(329,404,258),(508,604,250),(539,758,242),(550,452,226),(994,747,223),(935,379,219),(410,175,217),(291,639,193),(563,590,183),(289,318,160),(459,840,160),(710,851,149),(455,604,136),(904,223,133),(131,682,131),(425,692,120),(604,6,114),(408,72,112),(760,894,106),(984,435,95),(804,284,94),(630,502,89),(521,244,79),(288,822,74),(553,646,74),(489,145,73),(584,923,73),(984,405,59),(558,424,58),(75,56,55),(565,954,46),(71,432,45),(193,178,30),(941,652,23),(977,893,11),(194,370,4),(125,838,4),(473,797,4),(476,800,4),(527,853,4),(528,854,4),(126,610,3),(127,611,3),(284,610,3),(285,611,3),(698,391,3),(418,744,3),(422,746,3),(428,754,3),(432,756,3),(452,778,3),(456,780,3),(466,790,3),(468,794,3),(482,808,3),(488,814,3),(492,816,3),(512,838,3),(516,840,3),(525,849,3),(532,856,3),(592,916,3),(594,920,3),(628,954,3),(632,956,3),(397,723,2),(398,724,2),(399,725,2),(400,726,2),(401,727,2),(402,728,2),(403,729,2),(404,730,2),(405,731,2),(406,732,2),(408,734,2),(409,735,2),(410,736,2),(411,737,2),(412,738,2),(415,741,2),(416,742,2),(417,743,2),(422,748,2),(423,749,2),(424,750,2),(425,751,2),(426,752,2),(427,753,2),(432,758,2),(433,759,2),(434,760,2),(435,761,2),(436,762,2),(437,763,2),(438,764,2),(439,765,2),(440,766,2),(442,768,2),(443,769,2),(444,770,2),(445,771,2),(446,772,2),(447,773,2),(448,774,2),(450,776,2),(451,777,2),(456,782,2),(457,783,2),(458,784,2),(459,785,2),(460,786,2),(461,787,2),(462,788,2),(463,789,2),(464,790,2),(469,795,2),(470,796,2),(471,797,2),(476,802,2),(477,803,2),(478,804,2),(479,805,2),(481,807,2),(487,813,2),(492,818,2),(493,819,2),(494,820,2),(495,821,2),(496,822,2),(497,823,2),(498,824,2),(499,825,2),(500,826,2),(501,827,2),(504,830,2),(505,831,2),(506,832,2),(507,833,2),(508,834,2),(509,835,2),(510,836,2),(511,837,2),(516,842,2),(517,843,2),(518,844,2),(519,845,2),(520,846,2),(521,847,2),(522,848,2),(523,849,2),(532,858,2),(533,859,2),(534,860,2),(535,861,2),(536,862,2),(537,863,2),(538,864,2),(539,865,2),(540,866,2),(541,867,2),(542,868,2),(543,869,2),(544,870,2),(545,871,2),(546,872,2),(547,873,2),(548,874,2),(549,875,2),(550,876,2),(551,877,2),(552,878,2),(553,879,2),(554,880,2),(555,881,2),(556,882,2),(557,883,2),(558,884,2),(559,885,2),(560,886,2),(561,887,2),(562,888,2),(563,889,2),(564,890,2),(565,891,2),(566,892,2),(567,893,2),(568,894,2),(569,895,2),(570,896,2),(571,897,2),(572,898,2),(573,899,2),(574,900,2),(575,901,2),(576,902,2),(577,903,2),(578,904,2),(579,905,2),(580,906,2),(581,907,2),(582,908,2),(583,909,2),(584,910,2),(585,911,2),(586,912,2),(587,913,2),(588,914,2),(589,915,2),(590,916,2),(595,921,2),(596,922,2),(597,923,2),(598,924,2),(599,925,2),(600,926,2),(601,927,2),(602,928,2),(603,929,2),(604,930,2),(605,931,2),(606,932,2),(607,933,2),(608,934,2),(609,935,2),(610,936,2),(611,937,2),(612,938,2),(613,939,2),(614,940,2),(615,941,2),(616,942,2),(619,945,2),(620,946,2),(621,947,2),(622,948,2),(623,949,2),(624,950,2),(625,951,2),(626,952,2),(627,953,2),(632,958,2),(633,959,2),(634,960,2),(635,961,2),(636,962,2),(637,963,2),(638,964,2),(639,965,2),(640,966,2),(641,967,2),(642,968,2),(643,969,2),(644,970,2),(645,971,2),(646,972,2),(647,973,2),(648,974,2),(649,975,2),(650,976,2),(651,977,2),(652,978,2),(653,979,2),(654,980,2),(655,981,2),(656,982,2),(657,983,2),(658,984,2),(659,985,2),(660,986,2),(661,987,2),(662,988,2),(663,989,2),(665,991,2),(666,992,2),(667,993,2),(668,994,2),(669,995,2),(670,996,2),(671,997,2),(672,998,2),(794,990,2)],[(901,881,832),(888,843,629),(872,859,568),(668,937,468),(882,661,454),(703,815,415),(695,407,408),(468,454,371),(535,333,334),(697,872,301),(814,852,291),(348,899,258),(966,837,232),(779,659,216),(352,822,203),(856,701,200),(654,646,199),(427,423,186),(635,484,183),(908,180,181),(853,174,175),(983,174,175),(725,186,171),(786,507,160),(907,701,158),(455,729,150),(448,485,148),(671,657,143),(705,365,142),(878,430,137),(480,967,129),(643,581,128),(432,438,127),(894,115,116),(630,107,108),(781,100,101),(225,801,95),(703,89,90),(979,189,87),(770,428,80),(906,397,71),(996,683,59),(999,231,58),(837,847,55),(866,130,55),(945,135,52),(290,45,46),(241,705,30),(645,513,25),(672,501,19),(919,584,19),(76,645,10),(959,411,9),(529,122,4),(529,27,4),(146,148,3),(150,146,3),(168,126,3),(172,124,3),(176,120,3),(178,116,3),(196,98,3),(200,96,3),(216,78,3),(220,76,3),(258,38,3),(260,34,3),(268,26,3),(272,24,3),(143,151,2),(144,150,2),(145,149,2),(150,144,2),(151,143,2),(152,142,2),(153,141,2),(155,139,2),(156,138,2),(158,136,2),(159,135,2),(160,134,2),(161,133,2),(162,132,2),(163,131,2),(164,130,2),(165,129,2),(166,128,2),(167,127,2),(172,122,2),(173,121,2),(174,120,2),(179,115,2),(180,114,2),(181,113,2),(182,112,2),(183,111,2),(184,110,2),(185,109,2),(186,108,2),(187,107,2),(188,106,2),(189,105,2),(190,104,2),(191,103,2),(192,102,2),(193,101,2),(194,100,2),(195,99,2),(200,94,2),(201,93,2),(202,92,2),(203,91,2),(204,90,2),(205,89,2),(206,88,2),(207,87,2),(208,86,2),(209,85,2),(210,84,2),(211,83,2),(212,82,2),(213,81,2),(214,80,2),(215,79,2),(220,74,2),(221,73,2),(222,72,2),(223,71,2),(224,70,2),(225,69,2),(226,68,2),(227,67,2),(228,66,2),(229,65,2),(230,64,2),(231,63,2),(232,62,2),(233,61,2),(234,60,2),(235,59,2),(236,58,2),(237,57,2),(238,56,2),(239,55,2),(240,54,2),(241,53,2),(242,52,2),(243,51,2),(244,50,2),(245,49,2),(246,48,2),(247,47,2),(249,45,2),(250,44,2),(251,43,2),(252,42,2),(253,41,2),(254,40,2),(255,39,2),(256,38,2),(261,33,2),(262,32,2),(263,31,2),(264,30,2),(265,29,2),(266,28,2),(267,27,2),(272,22,2),(273,21,2),(274,20,2),(275,19,2),(276,18,2),(277,17,2),(278,16,2),(279,15,2),(280,14,2),(281,13,2),(282,12,2),(283,11,2),(284,10,2),(285,9,2),(286,8,2),(287,7,2),(288,6,2),(289,5,2),(290,4,2),(292,2,2),(293,1,2)]]
    mat = [['.']*1003 for _ in range(1003)]
    for i in range(4):
        for x in all[i]:
            sx, sy, cnt = x
            draw(mat, sx, sy, i, cnt)
    for x in mat:
        print(''.join(x))
    

def ten():
    a = ['', '0', '0 1']
    for i in range(25):
        a.append(a[-1]+' '+a[-2])

    print('a_i = a_{i-1} . a_{i-2}\n')

    for i in range(1, 9):
        print('a_{} = {}\n'.format(i, a[i]))

    print('a_9 = {}'.format(a[9][:80]))
    print('      {}\n'.format(a[9][80:]))

    for i in range(10, 16):
        print('a_{} = {}'.format(i, a[i][:80]))
        for j in range(80, len(a[i]), 80):
            print('       {}'.format(a[i][j:min(j+80, len(a[i]))]))
        print()

    print('\n(A_i)^n = B_i (mod 2)\n')


    inc =['','','O2','','H8VD1','NepgBq','I814pHCs1','2fdJdTJB7x4','owWrney7mOUXhC','7360jteUTGEFHw5yB','','hidg5hQTLnNXOCEOnitNXmLS1','QGDejvE8DCBTTErOr7gRxt6dr0E21','4G4cF7MhySata2jHrucqskOeuwX23osov','UjdjqetsRm0MDuJ4RyveQ9TXACtcnnA1ROwfXV','Dc2u067R9WI15XK90eaMh7NI91v2tkx0EfPVGWKaNrb1','5wBOdftDFbbale7b53DaoLef4Tm1kWWvum5eWZmU4oWF5CAg3','wmi12ylb5PS39lqQKhMbfEEgIJtkWBfhJtaes9dTVSIrnskjxgaRFa8','aYEdu3taWGQRl9pyVipEdsD0ckfI5el2ub2jcZClW9nCiJCt45Sp53YFdRKYJ','ZJLtuw8LvIFWvDjma8km7KW2f047pA2hcN5TygRJx5RAVdXZR801SbkpMZCtESkCZjO5','3u5D8gT1UTHM8Pt1fmROQT44fG6XHm','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']

    C = [[]for _ in range(71)]
    for i in range(len(inc)):
        C[i+1] = to2(from61(inc[i]), i+1)

    A = a[-1].split()
    for i in range(1, 71):
        B = []
        for j in range(i):
            B.append(A[j*i:(j+1)*i])
        for j in range(i):
            for k in range(i):
                B[j][k] = int(B[j][k])

        px = ''
        for j in range(i):
            fst = ' '*(6 if i < 10 else 7) if (i >>
                                            1) != j else 'A_{} = '.format(i)
            snd = ' '*(9 if i < 10 else 10) if (i >>
                                                1) != j else '   B_{} = '.format(i)
            aa = ' '.join(map(str, B[j]))
            bb = ' '.join(map(str, C[i][j]))
            px += fst + aa + snd + bb + '\n'
        print(px)
        

func = [zero, one, two, three, four, five, six, seven, eight, nine, ten]
func[int(input())]()