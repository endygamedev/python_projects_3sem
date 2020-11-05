"""
    Напишите рекурсивную функцию fib, вычисляющую n-ое число Фибоначчи
    fib внутри себя устанавливает случайный предел рекурсии (от 64 до 1000).
    Если вычисления не происходят из-за нарушения предела рекурсии, fib возвращает "не повезло".
"""

import sys
from random import randint


_DEFAULT_RECURSION_LIMIT = sys.getrecursionlimit()


def fib(n: int = 1) -> int:
    sys.setrecursionlimit(randint(64, 1001))
    return 1 if n < 3 else fib(n-1) + fib(n-2)


try:
    print(fib(30))
    print(fib(50))
except RecursionError:
    print('не повезло :(')