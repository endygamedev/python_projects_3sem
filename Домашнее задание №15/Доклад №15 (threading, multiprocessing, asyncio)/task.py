"""
    При помощи модуля threading создайте два потока, один поток пусть выполняет функцию сложения двух чисел, второй пусть умножает два числа.
"""


import threading


plus = lambda a, b: print(a+b)
times = lambda a, b: print(a*b)

threading.Thread(target=plus, args=(1, 2)).start()
threading.Thread(target=times, args=(1, 2)).start()
