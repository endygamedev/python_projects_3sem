'''
    С помощью модуля datetime определить дату, которая наступит через 10 дней от текущей даты.
'''


import datetime


print(datetime.date.today() + datetime.timedelta(10))
