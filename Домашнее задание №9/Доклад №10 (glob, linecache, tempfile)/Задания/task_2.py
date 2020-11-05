"""
    Возьмите произвольный текст и с помощью модуля linecache выведите из этого текста первую и последнюю строчку,
    несуществующую строчку (по номеру), а также попробуйте открыть файл, которого не существует.
"""


import linecache
import os
import tempfile


lorem = """Lorem ipsum dolor sit amet, consectetuer
adipiscing elit.  Vivamus eget elit. In posuere mi non
risus. Mauris id quam posuere lectus sollicitudin
varius. Praesent at mi. Nunc eu velit. Sed augue massa,
fermentum id, nonummy a, nonummy sit amet, ligula. Curabitur
eros pede, egestas at, ultricies ac, apellentesque eu,
tellus.

Sed sed odio sed mi luctus mollis. Integer et nulla ac augue
convallis accumsan. Ut felis. Donec lectus sapien, elementum
nec, condimentum ac, interdum non, tellus. Aenean viverra,
mauris vehicula semper porttitor, ipsum odio consectetuer
lorem, ac imperdiet eros odio a sapien. Nulla mauris tellus,
aliquam non, egestas a, nonummy et, erat. Vivamus sagittis
porttitor eros."""


def make_file(text: str) -> str:
    fd, temp_file_name = tempfile.mkstemp()
    os.close(fd)
    len_file_text = len(text.split('\n'))
    with open(temp_file_name, 'wt') as f:
        f.write(lorem)
    return temp_file_name, len_file_text


def clean_up(filename):
    os.unlink(filename)


def main():
    filename, len_file_text = make_file(lorem)

    print(f'Первая строчка: {linecache.getline(filename, 1)}')
    print(f'Последняя строка: {linecache.getline(filename, len_file_text)}')
    print(f'Пробую открыть файл, которого нет: {linecache.getline("PyThoN", 1)}')

    clean_up(filename)


main()