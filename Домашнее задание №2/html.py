''' Напишите декоратор html, который в результате вызова function('hi') записывает в файл с именем "my_file.html" следующий текст:

    2019/11/27 10:55
    <html>
    <strong>'hi'</strong>
    </html>

'''


def html(func):
    from time import gmtime, strftime
    def inner(*args, **kwargs):
        with open('my_file.html', 'w') as f:
            f.write(f'{strftime("%Y/%m/%d %H:%M", gmtime())}\n<html>\n<strong>{func(*args, **kwargs)}</strong>\n</html>')
        return func(*args, **kwargs)
    return inner


@html
def function(s = 'hello'):
    return s


print(function('hi'))
