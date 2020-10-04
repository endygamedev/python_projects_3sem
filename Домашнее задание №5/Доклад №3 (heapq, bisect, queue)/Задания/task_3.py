'''
    Создать очередь с приоритетом из 3 элементов, вывести ее. Затем добавить еще один элемент и вывести конечный вариант очереди.
'''


import queue


q = queue.PriorityQueue(3)

for i in range(3):
    q.put(i**2)

while not q.empty():
    print(q.get())

q.put(10**2)

while not q.empty():
    print(q.get())
