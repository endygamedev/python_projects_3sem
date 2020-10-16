'''
    Используя глубокое копирование, напишите функцию CountTill(), которая получает на вход число от 1 до 50, затем умножает его на два до тех пор, пока оно не превысит число 228, и на выход выдает два числа: исходное и полученное.
'''


import copy


x = int(input('Введите число от 1 до 50: '))

def CountTill(x: '0 < int < 51') -> tuple:

    copy_x = copy.deepcopy(x)

    while copy_x < 228: copy_x *= 2

    return x, copy_x


print(CountTill(x))
