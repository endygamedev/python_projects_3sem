'''
    Нужно ввести предложение и сделать динамическую границу вокруг этого предложения.
    Граница должна иметь ширину, которая вводится.
    Когда длина предложения превышает заданную ширину, необходимо напечатать новую строку и изменить высоту границы.
    Предложение также должно быть центрировано в динамической границе.
'''


import textwrap


sentence = input('Введите предложение: ')
width = int(input('Введите ширину строки: '))

# sentence = "You are only young once, but you can stay immature indefinitely."
# width = 26


def main(sentence: str, width: int) -> str:

    close_str = '+-' + '-' * width + '-+'

    lines = [sentence[i:width + i] for i in range(0, len(sentence), width)]

    print(close_str)

    for line in lines:
        print(f'| {line.center(width)} |')

    print(close_str)


main(sentence, width)
