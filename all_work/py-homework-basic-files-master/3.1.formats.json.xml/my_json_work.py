import json
from collections import Counter


with open('newsafr.json', 'rt', encoding='UTF-8') as file:
    json_file = json.load(file)
    list_of_news = json_file.get('rss').get('channel').get('items')
    counter_list = []
    for one_news in list_of_news:
        description_of_news = one_news.get('description')
        list_of_description = list(description_of_news.strip().split(' '))
        for description in list_of_description:
            if len(description) >= 6:
                counter_list.append(description)
    print(Counter(counter_list).most_common(10))
