import requests
import time
from diplom_2.user_params import user_params
from pprint import pprint


class MyExcept(Exception):
    pass


def get_params(token):
    params = {
        'v': '5.101',
        'access_token': token,
    }
    return params


"""Проверка что страница пользователя открыта"""


def check_user(user_id, token):
    try:
        response = get_request_for_get_list_of_id_groups(user_id, token)
        my_response = response.json()
        if 'error' in my_response.keys():
            if my_response.get('error').get('error_code') == 18:
                raise MyExcept
        flag = 0
        print('Пользователь найден')
    except MyExcept:
        flag = 1
        print('Страница удалена или заблокирована\n')
    return flag


"Проверка того что введенный адишник принадлежит заданому зарание пользователю"


def check_id_and_name_equal(input_for_test, user_id, token):
    params = get_params(token)
    split_input = input_for_test.split()
    print(split_input)
    params['user_ids'] = user_id
    response = requests.get(
        'https://api.vk.com/method/users.get',
        params=params
    )
    if split_input[0] in response.json()['response'][0]['first_name'] + '' \
            + response.json()['response'][0]['last_name']:
        if split_input[1] in response.json()['response'][0]['first_name'] + '' \
                + response.json()['response'][0]['last_name']:
            return True


"Нахождение ID пользователя по его никнейму"


def get_request_for_get_user_id(user_input, token):
    params = get_params(token)
    params['user_ids'] = user_input
    response = requests.get(
        'https://api.vk.com/method/users.get',
        params=params
    )
    return response


"Нахождение ID по полному имени пользователю"


def get_id_from_name(user_input, token):
    params = get_params(token)
    params['q'] = user_input
    input_for_test = user_input
    response = requests.get(
        'https://api.vk.com/method/users.search',
        params=params
    )
    pprint(response.json()['response'])
    if len(response.json()['response']) == 1:
        return response.json()['response'][0]['id'], input_for_test
    else:
        print('Найдено слишком много пользователей, для уточнения ответье на несколько вопросов')
        params['hometown'] = input('Город проживания (На русском языке): ')
        params['birth_year'] = input('День рождения (1-31): ')
        params['birth_year'] = input('Месяц рождения: ')
        params['birth_year'] = input('Год рождения: ')
        response = requests.get(
            'https://api.vk.com/method/users.search',
            params=params
        )
        if len(response.json()['response']) == 1:
            return response.json()['response'][0]['id'], input_for_test
        else:
            print('Такого пользователя нет или ошибка ввода параметров')
            print('Все еще много вариантов....')
            user_id = input('введите его ID: ')
            return user_id, input_for_test


"Получение параметров начального пользователя для дальнейшей работы"


def get_users_params(id_user, token):
    params = get_params(token)
    params['user_ids'] = id_user
    params['fields'] = ['books, can_see_audio, city, games, movies, music, sex, bdate']
    response = requests.get(
        'https://api.vk.com/method/users.get',
        params=params
    )
    return response


"Происк целей по заданым параметрам"


def search_list_users(token):
    used_user_params = user_params(token)
    params = get_params(token)
    params['city'] = used_user_params['city']
    if used_user_params['sex'] == 2:
        params['sex'] = '1'
    elif used_user_params['sex'] == 1:
        params['sex'] = '2'
    params['status'] = '6'
    params['age_from'] = used_user_params['years'] - 3
    params['age_to'] = used_user_params['years'] + 3
    params['has_photo'] = 1
    params['count'] = 1000
    params['fields'] = ['books, can_see_audio, city, games, movies, music, sex, bdate']
    # params['group_id'] = '1'
    response = requests.get(
        'https://api.vk.com/method/users.search',
        params=params
    )
    return response


"Обработка запроса на получение ID на правильность ввода"


def get_user_id(user_input, token):
    try:
        response = get_request_for_get_user_id(user_input, token)
        user_id = (response.json()['response'][0]['id'])
    except KeyError:
        print('Данного прользователя не существует\n')
        user_id = '-1'
    except IndexError:
        print('Не был введен пользователь')
        user_id = '-1'
    return user_id


"Запрос на получения списка групп"


def get_request_for_get_list_of_id_groups(id_user, token):
    params = get_params(token)
    params['user_id'] = id_user
    params['extended'] = '1',
    params['fields'] = 'members_count',
    params['count'] = '1000'
    response = requests.get(
        'https://api.vk.com/method/groups.get',
        params=params
    )
    return response


"Обработка запроса на получение списка групп"


def get_list_of_id_groups(id_user, token):
    try:
        response = get_request_for_get_list_of_id_groups(id_user, token)
        my_response = response.json()
        if 'error' in my_response.keys():
            if my_response.get('error').get('error_code') == 6:
                raise MyExcept('To many requests')
        list_user_groups = (response.json()['response']['items'])
    except MyExcept:
        print('Слишком много запросов, ждем 2 секунды перед повторным запросом')
        print('----------')
        time.sleep(2)
        response = get_request_for_get_list_of_id_groups(id_user, token)
        list_user_groups = (response.json()['response']['items'])
    return list_user_groups
