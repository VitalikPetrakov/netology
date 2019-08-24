""" TODO
Написать класс итератора, который по каждой стране из файла countries.json ищет страницу из википедии.
Записывает в файл пару: страна – ссылка.
Написать генератор, который принимает путь к файлу. При каждой итерации возвращает md5 хеш каждой строки файла.
"""

import json
import hashlib


# def read_file():
#     with open('countries.json', 'rt', encoding='utf8') as file:
#         data_in_file = json.load(file)
#     return data_in_file
#
# print(len(read_file()))

# def get_name_of_country(data_in_file):
#     for item in data_in_file:
#         name_of_country = item.get('name').get('common')
#         yield name_of_country


# def file_writer(path):
#     with open(path, 'w', encoding='utf8') as file:
#         for name in get_name_of_country(read_file()):
#             file.write(f'{name} - https://en.wikipedia.org/wiki/{name.replace(" ", "_")}\n')

class NameIter:
    def __init__(self):
        self.file_to_read = open('countries.json', 'rt', encoding='utf8')
        self.data = json.load(self.file_to_read)
        self.file_to_write = open('list_of_url.txt', 'w', encoding='utf8')
        self.n = len(self.data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.n == 0:
            self.file_to_write.close()
            self.file_to_read.close()
            raise StopIteration
        for item in self.data:
            self.name_of_country = item.get('name').get('common')
            self.file_to_write.write(f'{self.name_of_country} - https://en.wikipedia.org/wiki/'
                                     f'{self.name_of_country.replace(" ", "_")}\n')
            self.n -= 1
        return 'список стран готов'


def get_hash(path):
    file = open(path, 'rt', encoding='utf8')
    for line in file:
        line_hash = hashlib.md5(str(line).encode("utf-8")).hexdigest()
        yield line_hash
#
#
# if __name__ == '__main__':
#     path_of_file = 'list_of_url.txt'
#     file_writer(path_of_file)
#     for i in get_hash(path_of_file):
#         print(i)

if __name__ == '__main__':
    my_class = NameIter()
    for item in my_class:
        print(item)
    path_of_file = 'list_of_url.txt'
    for i in get_hash(path_of_file):
        print(i)