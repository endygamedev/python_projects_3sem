"""
    Создайте такую же структуру файлов, как указанно в начале, и с помощью модуля glob выведите одним ответом файлы file[.txt, filel.txt file2.txt, filea.txt
"""


from glob import glob


def main() -> None:
    for name in sorted(glob("dir/file*[[, l, 2 a].txt")):
        print(name)


main()