'''
    Дана строка, содержащая натуральные числа и слова.
    Необходимо сформировать список из чисел, содержащихся в этой строке.
    Например, задана строка "abc83 cde7 1 b 24".
    На выходе мы должны получить список [83, 7, 1, 24]
'''


import re


string = input('Введите строку: ')


def main(string: str) -> list:
    return list(map(lambda _: int(_), re.findall(r'\d+', string)))


print(main(string))


assert main('abc83 cde7 1 b 24') == [83, 7, 1, 24], 'Тест провален!'
