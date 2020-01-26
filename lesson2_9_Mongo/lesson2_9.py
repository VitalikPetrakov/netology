import csv
import re
from pymongo import MongoClient, ASCENDING
import pprint

client = MongoClient("mongodb://localhost:27017/")
netology_db = client['netology']
artist_collection = netology_db['artist']
result = artist_collection.remove()


def read_data(csv_file, db):
    with open(csv_file, encoding='utf8') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=',')
        for row in reader:
            db.insert_one(row)


def find_cheapest(db):
    """
    Отсортировать билеты из базы по возрастания цены
    Документация: https://docs.mongodb.com/manual/reference/method/cursor.sort/
    """
    sorted_db = list(db.artist.find().sort('Цена'))
    return sorted_db


def find_by_name(name, db):
    """
    Найти билеты по имени исполнителя (в том числе – по подстроке),
    и вернуть их по возрастанию цены
    """

    regex = re.compile('укажите регулярное выражение для поиска. ' \
                       'Обратите внимание, что в строке могут быть специальные символы, их нужно экранировать')
    find_in_db = list(db.artist.find({'Исполнитель': name}).sort('Цена'))
    return find_in_db



if __name__ == '__main__':
    read_data('artists.csv', netology_db['artist'])
    pp = pprint.PrettyPrinter(width=100, compact=True)
    # pp.pprint(list(artist_collection.find()))
    # pp.pprint(find_cheapest(netology_db))
    pp.pprint(find_by_name('Enter', netology_db))

