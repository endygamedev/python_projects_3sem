'''
    Дана произвольная строка. Вывести наименее часто встречающиеся элементы. (без использования reverse).
'''


from string import ascii_letters, digits
from random import randint, choice
import collections as cl


random_string = ''.join(choice(ascii_letters + digits) for _ in range(randint(5, 20)))
# random_string = 'aaabbbccddrrrr'
print('Исходная строка:', random_string)

n = len(set(random_string))
c = cl.Counter(random_string).most_common(n)

f_all_num = lambda lst, num: [element[num] for element in lst]

minimal_value = min(f_all_num(c, 1))

result = list(f_all_num(filter(lambda element: element[1] == minimal_value, c), 0))

print('Ответ:', result)
