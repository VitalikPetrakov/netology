"""
как должна работать программа
1)Ввод id пользователя (тот, чьи группы и друзей мы будем смотреть)
2)отправить запрос на получение множества ID групп
3)отправить запрос на получение списка ID друзей
4)создать пустое множество и перенести спискок групп объекта в него
5)создать пустое множество для групп друзей объекта
6)создать цикл, в котором будут перебераться список друзей
    6.1)у каждого друга вытаскивать списки их групп
    6.2)каждый список добавилять в множество групп друзей обекта
7) через символ - сопоставить множества
8) отправить запрос на получение информации по группе из оставшихся групп из пункта 7
9) приобразовать вывод
10) записать в файл
"""

from pprint import pprint

import requests
import time

token = ''

set_id_user_groups = set()
set_id_friends_groups = set()
user_id = input('Введите ID пользователя ВК:')

def get_list_of_friends(id_user):
    response = requests.get(
        'https://api.vk.com/method/friends.get',
        params={
            'access_token': token,
            'v': '5.101',
            'user_id': id_user,
        }
    )
    list_user_friends = (response.json()['response']['items'])
    return list_user_friends


def get_list_of_id_groups(id_user):
    response = requests.get(
        'https://api.vk.com/method/groups.get',
        params={
            'access_token': token,
            'v': '5.101',
            'user_id': id_user,
            'extended': '1',
            'fields': 'members_count',
            'count': '1000'
        }
    )
    list_user_groups = (response.json()['response']['items'])
    time.sleep(0.5)
    return list_user_groups


def get_set_of_id_friends_groups(user_id):
    list_user_friends = get_list_of_friends(user_id)
    i = 1
    print(f'Колличество друзей у пользователя: {len(list_user_friends)}')
    for friend in list_user_friends:
        try:
            list_user_groups = get_list_of_id_groups(friend)
            for group in list_user_groups:
                set_id_friends_groups.add(group['id'])
            print(f'Подсчет групп у пользователя под номером {i}')
            i += 1
            print('----------')
        except:
            print(f'Проблема со страницей у пользователя под номером (возможно страница удалена) {i}')
            print('----------')
            i += 1
            continue
    print(f'Общее колличество групп у друзей пользователя: {len(set_id_friends_groups)}')
    return set_id_friends_groups


def get_set_of_id_user_groups(user_id):
    list_of_groups = get_list_of_id_groups(user_id)
    for group in list_of_groups:
        set_id_user_groups.add(group['id'])
    return set_id_user_groups


def get_general_groups():
    general_groups = get_set_of_id_user_groups(user_id) - get_set_of_id_friends_groups(user_id)
    return general_groups


print(f'Колличество групп, в которых нет друзей пользователя: {len(get_general_groups())}')
print(f'Общее колличество групп у пользователя: {len(get_set_of_id_user_groups(user_id))}')
