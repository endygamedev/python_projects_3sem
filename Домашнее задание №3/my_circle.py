'''
    Определите класс MyCircle, который принимает два аргумента: последовательность и число.
    Объект будет возвращать элементы заданное число раз. Если число больше количества элементов, то последовательность повторяется по мере необходимости.
    Определить класс так, чтобы он использовал MyCircleIterator, т.е. multiclass iterators.

'''


class MyCircle:
    def __init__(self, iterable, n):
        # print('\t __init__ для MyCircle')
        self.iterable = iterable
        self.n = n

    def __iter__(self):
        # print('\t __iter__ для MyCircle')
        return MyCircleIterator(self.iterable, self.n)

class MyCircleIterator:
    def __init__(self, iterable, n):
        # print('\t __init__ для MyCircleIterator')
        self.iterable = iterable
        self.n = n
        self.i = 0

    def __iter__(self):
        # print('\t __iter__ для MyCircleIterator')
        return self

    def __next__(self):
        # print('\t __next__ для MyCircleIterator')
        if self.i < self.n:
            i = self.i
            self.i += 1
            return self.iterable[i % len(self.iterable)]
        else:
            raise StopIteration


c = MyCircle('abc', 5)
print(list(c))
