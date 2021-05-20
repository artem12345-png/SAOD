import random
import timeit

time = []


def Dijkstra(N, S, matrix):
    ts = 0
    ts = timeit.default_timer()
    valid = [True for i in range(N)]
    weight = [1000000 for i in range(N)]
    weight[S] = 0
    for i in range(N):
        min_weight = 1000001
        ID_min_weight = -1
        for j in range(N):
            if valid[j] and weight[j] < min_weight:
                min_weight = weight[j]
                ID_min_weight = j
        for z in range(N):
            if weight[ID_min_weight] + matrix[ID_min_weight][z] < weight[z]:
                weight[z] = weight[ID_min_weight] + matrix[ID_min_weight][z]
        valid[ID_min_weight] = False
    time.append(timeit.default_timer() - ts)
    return weight


"""
Заполнение матрицы смежности
"""

ls = [[0 for j in range(20)] for i in range(20)]
for i in range(20):
    for j in range(20):
        if i == j:
            ls[i][j] = 0
        else:
            ls[i][j] = random.randint(1, 10)
            ls[j][i] = ls[i][j]

ls_2 = [[100000 for i in range(10000)] for i in range(10000)]
helper = [[0 for i in range(100)] for i in range(100)]
counter = 0
k = 0

for i in range(100):
    for j in range(100):
        if (i - 1) < 0 and (j - 1) < 0:
            ls_2[counter][k + 1] = random.randint(1, 10)
            ls_2[counter][k + 100] = random.randint(1, 10)

        elif (i - 1) < 0 and (j + 1) == 100:
            ls_2[counter][k - 1] = random.randint(1, 10)
            ls_2[counter][k + 100] = random.randint(1, 10)

        elif (i - 1) < 0:
            ls_2[counter][k- 1] = random.randint(1, 10)
            ls_2[counter][k + 1] = random.randint(1, 10)
            ls_2[counter][k + 100] = random.randint(1, 10)

        elif (i + 1) == 100 and (j - 1) == 0:
            ls_2[counter][k + 1] = random.randint(1, 10)
            ls_2[counter][k - 100] = random.randint(1, 10)

        elif (i + 1) == 100 and (j + 1) == 100:
            ls_2[counter][k - 1] = random.randint(1, 10)
            ls_2[counter][k - 100] = random.randint(1, 10)

        elif (i + 1) == 100:
            ls_2[counter][k + 1] = random.randint(1, 10)
            ls_2[counter][k - 100] = random.randint(1, 10)
            ls_2[counter][k - 1] = random.randint(1, 10)

        elif (j - 1) < 0:
            ls_2[counter][k + 1] = random.randint(1, 10)
            ls_2[counter][k + 100] = random.randint(1, 10)
            ls_2[counter][k - 100] = random.randint(1, 10)

        elif (j + 1) == 100:
            ls_2[counter][k - 1] = random.randint(1, 10)
            ls_2[counter][k + 100] = random.randint(1, 10)
            ls_2[counter][k - 100] = random.randint(1, 10)

        else:
            ls_2[counter][k - 1] = random.randint(1, 10)
            ls_2[counter][k + 1] = random.randint(1, 10)
            ls_2[counter][k + 100] = random.randint(1, 10)
            ls_2[counter][k - 100] = random.randint(1, 10)
        counter += 1
        k += 1

p1 = Dijkstra(len(ls), 0, ls)
p2 = Dijkstra(len(ls_2), 0, ls_2)

heap1 = [0 for i in range(len(p1))]
heap2 = [0 for i in range(len(p2))]


def heap(ls_helper, element, i):
    if ls_helper[i] == 0:
        ls_helper[i] = element

    elif ls_helper[i] >= element:
        i = 2 * i + 1
        heap(ls_helper, element, i)
    else:
        i = 2 * i + 2
        heap(ls_helper, element, i)


k = -1

for item in p1:
    k += 1
    heap(heap1, item, k)

k = -1
for item in p2:
    k += 1
    heap(heap2, item, k)
print(time)
print(p1)
print(p2)
