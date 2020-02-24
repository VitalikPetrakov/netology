""" TODO
Написать класс итератора, который по каждой стране из файла countries.json ищет страницу из википедии.
Записывает в файл пару: страна – ссылка.
Написать генератор, который принимает путь к файлу. При каждой итерации возвращает md5 хеш каждой строки файла.
"""

import json
import hashlib


class NameIter:
    def __init__(self):
        self.file_to_read = open('countries.json', 'rt', encoding='utf8')
        self.data = json.load(self.file_to_read)
        self.file_to_write = open('list_of_url.txt', 'w', encoding='utf8')
        self.n = len(self.data)
        self.idx=0
        self.file_to_read.close()  

    def __iter__(self):
        return self

    def __next__(self):
        item=self.data[self.idx]
        self.name_of_country = item.get('name').get('common')
        self.file_to_write.write(f'{self.name_of_country} - https://en.wikipedia.org/wiki/'
                                 f'{self.name_of_country.replace(" ", "_")}\n')
        self.idx+=1
        if self.idx==self.n:
            self.file_to_write.close()
            raise StopIteration
        return item

        
   """  
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
"""

def get_hash(path):
    file = open(path, 'rt', encoding='utf8')
    for line in file:
        line_hash = hashlib.md5(str(line).encode("utf-8")).hexdigest()
        yield line_hash


if __name__ == '__main__':
    my_class = NameIter()
    for item in my_class:
        #print(item)
        pass                         
    path_of_file = 'list_of_url.txt'
    for i in get_hash(path_of_file):
        print(i)
