'''
    При помощи модуля calendar вывести календарь на 2021 год в виде HTML таблицы в файле под названием "my_calendar". А также выяснить, является ли 2021 високостным.
'''


import calendar


calend = calendar.HTMLCalendar(firstweekday = 0)

c = calend.formatyear(2021, width = 3)

with open('my_calendar.html', 'w') as html_file:
    html_file.write(c)


def leapQ(year: int) -> str:
    return 'Год високосный' if calendar.isleap(year) else 'Год невисикосный'


print(leapQ(2021))
