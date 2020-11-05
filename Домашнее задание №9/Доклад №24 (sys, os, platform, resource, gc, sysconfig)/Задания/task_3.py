"""
    Получите имя папки в текущей директории, в которой меньше всего файлов
"""


import os
import shutil
from typing import List, Tuple


def create_folders(folder_list: List[str]) -> None:
    for folder in folder_list:
        os.makedirs(os.getcwd()+folder)


def create_files(files_dirs: Tuple[str]) -> None:
    for file in files_dirs:
        with open(os.getcwd()+file, 'w', encoding='UTF-8') as f:
            f.write('*тут могла быть ваша реклама...*')


def delete_folders(folder_list: List[str]) -> None:
    for folder in folder_list:
        shutil.rmtree(os.getcwd()+folder, ignore_errors=True)


def count_files(folder_list: List[str]) -> None:
    return {os.getcwd()+folder: len(os.listdir(os.getcwd()+folder)) for folder in folder_list}


folder_list = ['/Folder 1', '/Folder 2']
file_dirs = ('/Folder 1/some text 1.txt', '/Folder 1/some text 2.txt', '/Folder 1/some text 3.txt',
             '/Folder 2/some text 1.txt', '/Folder 2/some text 2.txt')


def main(folder_list: List[str], file_dirs: Tuple[str]) -> str:
    create_folders(folder_list)
    create_files(file_dirs)
    d = count_files(folder_list)
    delete_folders(folder_list)
    return min(d, key=d.get)


print(main(folder_list, file_dirs))