import xml.etree.ElementTree as ET
from collections import Counter
import json

file = 'newsafr.xml'

tree = ET.parse(file)
root = tree.getroot()
counter_list = []

for elem in root:
    for subelem in elem:
        if subelem.tag == 'item':
            list_of_description = list(subelem[2].text.strip().split(' '))
            for description in list_of_description:
                if len(description) >= 6:
                    counter_list.append(description.lower())
    print(Counter(counter_list).most_common(10))



with open('newsafr.json', 'rt', encoding='UTF-8') as file:
    json_file = json.load(file)
    list_of_news = json_file.get('rss').get('channel').get('items')
    counter_list = []
    for one_news in list_of_news:
        description_of_news = one_news.get('description')
        list_of_description = list(description_of_news.strip().split(' '))
        for description in list_of_description:
            if len(description) >= 6:
                counter_list.append(description.lower())
    print(Counter(counter_list).most_common(10))