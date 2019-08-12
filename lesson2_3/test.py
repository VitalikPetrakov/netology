import json
import hashlib
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


@log_with_path('log1.txt')
def read_file():
    with open('countries.json', 'rt', encoding='utf8') as file:
        data_in_file = json.load(file)
    return data_in_file


@log_with_path('log2.txt')
def get_name_of_country(data_in_file):
    for item in data_in_file:
        name_of_country = item.get('name').get('common')
        name_of_country = name_of_country
        yield name_of_country


@log_with_path('log1.txt')
def file_writer(path):
    with open(path, 'w', encoding='utf8') as file:
        for name in get_name_of_country(read_file()):
            file.write(f'{name} - https://en.wikipedia.org/wiki/{name.replace(" ", "_")}\n')


@log_with_path('log2.txt')
def get_hash(path):
    file = open(path, 'rt', encoding='utf8')
    for line in file:
        line_hash = hashlib.md5(str(line).encode("utf-8")).hexdigest()
        yield line_hash


if __name__ == '__main__':
    path_of_file = 'list_of_url.txt'
    file_writer(path_of_file)
    for i in get_hash(path_of_file):
        print(i)

