"""
    Отформатировать числа (321.3, 12345.8974) в (321,3 zł, 12345,90 zł) - Польский злотый
"""


import locale


numbers = (321.3, 12345.8974)
locale.setlocale(locale.LC_ALL, 'pl_PL')

print(tuple(map(locale.currency, numbers)))