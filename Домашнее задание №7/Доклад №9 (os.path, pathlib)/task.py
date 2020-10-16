'''
    Используя модули os.path и pathlib, создать в текущей рабочей директории папку Path.example, в данной папке создать тектовый файл ExampleTextFile, в котором будет написано Образец данных для записи в файл.
'''


import os
from pathlib import Path


def main() -> str:
    try:
        current_path = os.path.join(Path.cwd(), 'Path.example')
        os.mkdir(current_path)
        txt_file = Path(os.path.join(current_path, 'ExampleTextFile.txt'))
        txt_file.write_text('Образец данных для записи в файл')
        return 'Файл создан в папке Path.example'
    except Exception as e:
        return f'Ошибка: {e}'


print(main())
