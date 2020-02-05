import csv
import re
from pymongo import MongoClient
import pprint

client = MongoClient("mongodb://localhost:27017/")
netology_db = client['netology']
artist_collection = netology_db['artist']
result = artist_collection.remove()


def read_data(csv_file, db):
    with open(csv_file, encoding='utf8') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=',')
        for row in reader:
            row['Цена'] = int(row['Цена'])
            db.insert_one(row)
    return reader


def find_cheapest(db):
    sorted_db = list(db.artist.find().sort('Цена'))
    return sorted_db


def find_by_name(name, db):
    regex = re.compile('.*(' + name + ').*', re.I)
    print(regex)
    find_in_db = list(db.artist.find({'Исполнитель': regex}, {"_id": 0}))
    return find_in_db


if __name__ == '__main__':
    read_data('artists.csv', netology_db['artist'])
    pp = pprint.PrettyPrinter(width=100, compact=True)
    # pp.pprint(find_cheapest(netology_db))
    print(find_by_name('Fest', netology_db))



