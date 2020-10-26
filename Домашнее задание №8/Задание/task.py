"""
    С помощью представленных модулей выполнить следующие задания:
       1) предварительно создать в текущей директории произвольный текстовый файл, с которым будем работать
       2) скопировать файл в другой файл и проверить, что они совпадают
       3) создать архив из скопированного файла
       4) с помощью mmap прочитать изначальный файл (получится байт строка) и декодировать её (дабы избежать ошибок, рекомендую использовать errors = "ignore")
"""


import shutil as sh
import filecmp as fl
import os
import mmap
import codecs as cd


def main() -> None:
    sh.copyfile('some_text.txt', 'some_text_copy.txt', follow_symlinks=True)            # скопировал файл
    print(f"Совпадают ли файлы ? - {fl.cmp('some_text.txt', 'some_text_copy.txt')}")    # проврка на совпадение файлов

    sh.make_archive('some_archive', 'zip', os.getcwd())                                 # создаём архив

    with open('some_text.txt', 'r', encoding='utf-8') as file:                          # прочитал изначальный файл
        with mmap.mmap(file.fileno(), length=0, access=mmap.ACCESS_READ) as mmap_obj:
            text_mmap = mmap_obj.read()

    print(text_mmap)

    print(cd.decode(text_mmap, encoding='utf-8', errors='ignore'))                      # декодируем байт строку


main()