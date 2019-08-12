"""TODO
Написать декоратор - логгер. Он записывает в файл дату и время вызова функции, имя функции, аргументы, с которыми вызвалась и возвращаемое значение.
Написать декоратора из п.1 но с параметром – пути к логам.
Применить написанный логгер к приложению из любого предыдущего д/з.
"""

from datetime import datetime


def log_with_path(path):
    def logger(old_func):
        def new_func(*args, **kwargs):
            with open(path, 'a', encoding='utf8') as file:
                result = old_func(*args, **kwargs)
                file.write(f'{datetime.now()} {old_func.__name__} !{str(args)} !!{str(kwargs)}\n {result}\n')
            return result
        return new_func
    return logger