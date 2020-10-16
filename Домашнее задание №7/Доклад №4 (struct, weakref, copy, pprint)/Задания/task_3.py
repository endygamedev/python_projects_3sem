'''
    Убедиться в том, что невозможно создать ссылку на объект типа int и придумать, как это ограничение можно обойти с помощью классов
'''


import weakref


d = weakref.WeakValueDictionary()

d['error'] = 10
print(d['error'])

'''
    Да, это действительно не работает! Я пытался обойти эту проблему наследованием класса int, но это не помогло ... :(
    Я посмотрел документацию и там написано 'CPython implementation detail: Other built-in types such as tuple and int do not support weak references even when subclassed.'
    К сожалению, эта задача нерешаемая, либо я не так понял.

    Ссылка на документацию: https://docs.python.org/3/library/weakref.html
'''
