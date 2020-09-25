'''
    С помощью модуля statistics найдите population variance и population standart deviation от последовательности среднего арифметического, среднего геометрического и среднего гармонического от 30 случайных чисел.
'''


from random import randint
import statistics as st


lst = [randint(1, 100) for _ in range(30)]
lst_mean = [st.mean(lst), st.geometric_mean(lst), st.harmonic_mean(lst)]

print(f'Population variance: {st.pvariance(lst_mean)}')
print(f'Population standart deviation: {st.pstdev(lst_mean)}')
