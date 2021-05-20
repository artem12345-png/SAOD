import random
import timeit
import operator
import matplotlib.pyplot as plt
import numpy as np

col_KR = [0 for i in range(200009)]  # для колизий
col_XOR = [0 for i in range(200009)]  # для колизий
sum_col_KR = []  # для суммы колизий
sum_col_XOR = []  # для суммы колизий
tl = []  # for time
elements_list = [i for i in range(21)]  # количество замеров
t = 0
k = -1
ls = ['' for i in range(500000)]  # количество слов
ls[0] = 'Аале'
f = open('words.txt')
KR_l = [[] for i in range(200009)]  # список начлаьный в хештаблице
XOR_l = [[] for i in range(200009)]  # список начлаьный в хештаблице
KR_t = []  # список для времени поиска в хештаблице
XOR_t = []  # список для времени поиска в хештаблице


def tree(line, i):
    if ls[i] == '':
        ls[i] = line
    elif ls[i] >= line:
        i = 2 * i + 1
        tree(line, i)
    else:
        i = 2 * i + 2
        tree(line, i)


def look_up(line, i):
    t = 0
    t = timeit.default_timer()
    if ls[i] == line:
        tl.append(timeit.default_timer() - t)
    elif ls[i] >= line:
        i = 2 * i + 1
        look_up(line, i)
    else:
        i = 2 * i + 2
        look_up(line, i)


def KRHash(line):
    h = 0
    hash_mul = 31
    h = sum([ord(c) for c in line]) + 1 + h * hash_mul

    return h % len(KR_l)


def XOR(line):
    h = 0
    h = operator.xor(h, sum([ord(c) for c in line]))
    return h % len(XOR_l)


def KR_hash_table(line, col_KR):
    KR_l[KRHash(line)].append(line)
    col_KR[KRHash(line)] += 1


def KR_look_up(line):
    t = 0
    t = timeit.default_timer()
    if line in KR_l[KRHash(line)]:
        KR_t.append(timeit.default_timer() - t)


def XOR_look_up(line):
    t = 0
    t = timeit.default_timer()
    if line in XOR_l[XOR(line)]:
        XOR_t.append(timeit.default_timer() - t)


def XOR_hash_table(line, col_XOR):
    XOR_l[XOR(line)].append(line)
    col_XOR[XOR(line)] += 1


for line in f:

    k += 1
    tree(line, k)
    KR_hash_table(line, col_KR)
    XOR_hash_table(line, col_XOR)
    if (k % 10000) == 0:
        look_up(line, k)
        XOR_look_up(line)
        KR_look_up(line)

        sum_col_XOR.append(sum(col_XOR))
        sum_col_KR.append(sum(col_KR))

        col_KR.clear()
        col_KR = [0 for i in range(200009)]
        col_XOR.clear()
        col_XOR = [0 for i in range(200009)]

    if k == 200000:
        break

# random.shuffle(ls)
print(sum_col_XOR, '\n', sum_col_KR, '\n')




print(len(sum_col_XOR), '\n', len(elements_list))
fig, ax = plt.subplots()
ax.plot(elements_list, sum_col_KR)
ax.plot(elements_list, sum_col_XOR)
#ax.plot(xS, y)
#ax.plot(xT, y)
plt.show()
