"""
    Не используя библеотеку UUID создать уникальную 12-ти символьную строку, используя латиницу, цифры, а также сегодняшнюю дату и время.
"""


from string import digits, ascii_uppercase
from random import choice, sample
from time import localtime, strftime


def main():
    s = [*(choice(ascii_uppercase + digits) for _ in range(8)), strftime('%d', localtime()), strftime('%H', localtime())]
    return ''.join(sample(s, len(s)))

print(main())