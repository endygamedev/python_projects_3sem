'''
    Создать отсортированный список из 10 элементов, ввести некоторое чисто а. Найти позицию а, если вставлять его в список как можно правее, а затем добавить его в список как можно левее.
'''


import bisect
from random import randint


rand_list = sorted([randint(-10, 10) for _ in range(10)])

print(rand_list)

a = int(input('Введите некоторое число a: '))

bisect.insort(rand_list, a)
print(rand_list)

bisect.insort_left(rand_list, a)
print(rand_list)

pos = bisect.bisect(rand_list, a)
print(pos)
