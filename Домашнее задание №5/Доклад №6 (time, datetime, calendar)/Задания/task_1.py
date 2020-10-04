'''
    При помощи модуля time преобразовать текущее время в число секунд с начала эпохи, не используя метод time().
'''


import time


print(time.mktime(time.localtime()))
