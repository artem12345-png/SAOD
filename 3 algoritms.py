import timeit
import random
import matplotlib.pyplot as plt
import numpy as np






# Метод сортировки Radix Sort
def Radix_sort(list1):
    list = list1
    long = len(list)
    r = 1
    max_element = max(list)
    is_check = True
    ts = 0
    fin_ls = [0 for i in range(len(list))]

    ts = timeit.default_timer()

    while ((max_element // r) > 0):

        counter = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

        for element in list:
            counter[int((element / r) % 10)] += 1

        for i in range(1, len(counter)):
            counter[i] = counter[i] + counter[i - 1]

        list.reverse()

        for element in list:
            fin_ls[counter[int((element / r) % 10)] - 1] = element
            counter[int((element / r) % 10)] -= 1
        r*=10

        list = fin_ls
        fin_ls = [0 for i in range(len(list))]
    xR.append(timeit.default_timer() - ts)
        # Проверка корректной сортировки
    for i in range(long - 1):
        if fin_ls[i] > fin_ls[i + 1]:
            is_check = False

    if is_check:
        print("Radix Sort successful")
    else:
        print('Radix Sort ERROR!!!')
    return


# Метод сортировки Selection Sort
def Selection_Sort(list1):
    list = list1
    # Переменная для подсчета времени сортировки
    ts = 0
    long = len(list)
    # Переменная для проверки правильной сортировки
    is_check = True

    # Запуск таймера
    ts = timeit.default_timer()

    # Начало сортировки
    for i in range(long - 1):
        smallest = i

        for j in range(i + 1, long):
            if list[j] < list[smallest] :
                smallest = j

        list[i], list[smallest] = list[smallest], list[i]

    # Вывод затраченого времени для сортировки
    xS.append(timeit.default_timer() - ts)

    # Проверка корректной сортировки
    for i in range(long - 1):
        if list[i] > list[i + 1]:
            is_check = False

    if is_check :
        print("Selection Sort successful")
    else:
        print('Selection Sort ERROR!!!')



# Метод сортировки Heap Sort
def Heap_Sort(list1):
    list = list1
    long = len(list)
    ts = 0
    ts = timeit.default_timer()
    is_check = True
    for i in range(long // 2 - 1, -1, -1):
        Heapify(list, long, i)

    for i in range(long - 1, 0, -1):
        list[0], list[i] = list[i], list[0]
        Heapify(list, i, 0)
    xH.append(timeit.default_timer() - ts)

    # Проверка корректной сортировки
    for i in range(long - 1):
        if list[i] > list[i + 1]:
            is_check = False

    if is_check:
        print("Heap Sort successful")
    else:
        print('Heap Sort ERROR!!!')


def Heapify(list, long, i):
    max_el = i

    l = 2 * i + 1
    r = 2 * i + 2

    if ((l < long) and (list[l] > list[max_el])):
        max_el = l

    if ((r < long) and (list[r] > list[max_el])):
        max_el = r

    if (max_el != i):
        list[i], list[max_el] = list[max_el], list[i]
        Heapify(list, long, max_el)


def test(list1):
    list = list1
    ts = 0
    ts = timeit.default_timer()
    list.sort()
    xT.append(timeit.default_timer() - ts)







y = []
xH = []
xR = []
xS = []
xT = []
list = []


for i in range(50000, 1050000, 50000):
    list1 = [random.randint(0, 100000) for j in range(i)]
    Radix_sort(list1)
    Selection_Sort(list1)
    Heap_Sort(list1)
    test(list1)

    y.append(i)

print(xH)
print(xS)
print(xT)
print(xR)

fig, ax = plt.subplots()
ax.plot(xH, y)
ax.plot(xR, y)
ax.plot(xS, y)
ax.plot(xT, y)
plt.show()




