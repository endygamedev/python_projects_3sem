"""
    Испльзуя класс Popen запустите процесс notepad.exe передайте процессу timeout=3, если процесс завершится до истечения времени,
    то выведите строчку "Успех!", иначе отловите ошибку TimeoutExpired и вывидите "Провал!"
"""


import subprocess


try:
    with subprocess.Popen(['notepad.exe']) as proc:
        proc.communicate(input=None, timeout=3)
    print('Успех!')
except subprocess.TimeoutExpired:
    print('Провал!')