"""
    Определите, сколько лет назад был собран Ваш интерпретатор. Выведите "пора обновиться", если интерпретатору не 0 лет.
"""


import platform
from datetime import datetime


def main() -> None:
   interpreter_year = datetime.strptime(platform.python_build()[1], "%b %d %Y %H:%M:%S").year
   now_year =datetime.now().year
   return 'добре' if now_year - interpreter_year == 0 else 'пора обновляться'


print(main())