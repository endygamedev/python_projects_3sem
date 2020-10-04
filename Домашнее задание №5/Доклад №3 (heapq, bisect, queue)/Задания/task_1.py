'''
    Создать кучу из 10 случайных чисел и вывести наименьшие числа с 4 по 6 (порядковые номера изначальной кучу).
'''


import heapq
from random import randint


rand_list = [randint(0, 10) for _ in range(10)]
print(rand_list)
heapq.heapify(rand_list)
print(rand_list)
print(heapq.nsmallest(6, rand_list)[3:6])
