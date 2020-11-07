"""
    С помощью модуля trace создайте отчет о работе любой функции, сохраните этот отчет в формате txt, при этом подсчет числа линий и выполнение линий трассировки должны быть включены.
"""


import trace


def fibonacci(n: int = 1):
    return 1 if n < 3 else fibonacci(n-1)+fibonacci(n-2)


tracer = trace.Trace(count=True, trace=True)
tracer.runfunc(fibonacci, 20)
results = tracer.results()
results.write_results()