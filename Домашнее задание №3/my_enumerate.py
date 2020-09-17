'''

    Создайте свой собственный класс MyEnumerate двумя способами (обычный и multiclass iterators), чтобы использовать его вместо enumerate.
    MyEnumerate должен будет возвращать кортеж при каждой итерации, причем первый элемент в кортеже является индексом (начиная с 0), а второй элемент является текущим элементом из базовой структуры данных.
    Попытка использовать MyEnumerate с noniterable аргументом приведет к ошибке.

'''


# 1 способ (обычный)
class MyEnumerateClassic:
    def __init__(self, iterable):
        #print('\t __init__ для MyEnumerateClassic')
        self.iterable = iterable
        self.i = 0

    def __iter__(self):
        #print('\t __iter__ для MyEnumerateClassic')
        return self

    def __next__(self):
        #print('\t __next__ для MyEnumerateClassic')
        if self.i < len(self.iterable):
            i = self.i
            self.i += 1
            return (i, self.iterable[i])
        else:
            raise StopIteration


print('Обычный метод MyEnumerateClassic'.center(50, '-'))

for index, letter in MyEnumerateClassic('abc'):
    print(f'{index}: {letter}')

my_enum = MyEnumerateClassic('abc')
print(f'MyEnumerateClassic: {dict(my_enum)}')            # всё будет хорошо
print(f'MyEnumerateClassic: {dict(my_enum)}')            # получим пустой список


# 2 способ (multiclass iterators)
class MyEnumerateMulticlass:
    def __init__(self, iterable):
        #print('\t __init__ для MyEnumerateMulticlass')
        self.iterable = iterable

    def __iter__(self):
        #print('\t __iter__ для MyEnumerateMulticlass')
        return MyEnumerateIterator(self.iterable)

class MyEnumerateIterator:
    def __init__(self, iterable):
        #print('\t __init__ для MyEnumerateIterator')
        self.iterable = iterable
        self.i = 0

    def __iter__(self):
        #print('\t __iter__ для MyEnumerateIterator')
        return self

    def __next__(self):
        #print('\t __next__ для MyEnumerateIterator')
        if self.i < len(self.iterable):
            i = self.i
            self.i += 1
            return (i, self.iterable[i])
        else:
            raise StopIteration


print('\n'+'Multiclass метод MyEnumerateMulticlass'.center(50, '-'))

for index, letter in MyEnumerateMulticlass('abc'):
    print(f'{index}: {letter}')

my_enum_multi = MyEnumerateMulticlass('abc')
print(f'MyEnumerateMulticlass: {dict(my_enum_multi)}')      # всё будет хорошо
print(f'MyEnumerateMultuclass: {dict(my_enum_multi)}')      # всё будет хорошо
