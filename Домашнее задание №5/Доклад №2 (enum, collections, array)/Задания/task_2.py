'''
    С помощью каждого из первых двух изученных модулей создать массивы из 5 переменных с некоторыми значениями, увеличить каждое значение в три раза и добавить новый элемент со значением 1.
'''


from enum import Enum
from array import *
import collections as cl


class Numbers(Enum):
    var1 = 1
    var2 = 2
    var3 = 3
    var4 = 4
    var5 = 5

arr_enum = array('i', [])

for element, value in Numbers.__members__.items():
    arr_enum.append(Numbers[element].value * 3)
arr_enum.append(1)

print('Массив полученный через Enum: '.center(40, ' '))
print(arr_enum)


arr_collections = array('i', [])

c = cl.Counter(var1 = 1, var2 = 2, var3 = 3, var4 = 4, var5 = 5)

for element in c:
    arr_collections.append(c[element] * 3)

arr_collections.append(1)

print('\n' + 'Массив полученный через Collections: '.center(48, ' '))
print(arr_collections)
