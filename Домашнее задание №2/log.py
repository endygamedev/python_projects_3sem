'''Напишите декоратор log
>>> @log
... def function(*args):
...... return 3 + len(args)

>>> function(4, 4, 4)
вы вызвали функцию function(4, 4, 4)
она вернула значение 6
6
'''


def log(func):
    def inner(*args, **kwargs):
        print(f'вы вызвали функцию {func.__name__}{args}')
        print(f'она вернула значение {func(*args, **kwargs)}')
        return func(*args, **kwargs)
    return inner

@log
def function(*args):
    return 3 + len(args)

print(function(4, 4, 4))
