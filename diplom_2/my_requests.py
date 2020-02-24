import requests
import time


class MyExcept(Exception):
    pass


def get_params(token):
    params = {
        'v': '5.101',
        'access_token': token,
    }
    return params


def check_user(user_id, token):
    try:
        response = get_request_for_get_list_of_id_groups(user_id, token)
        my_response = response.json()
        if 'error' in my_response.keys():
            if my_response.get('error').get('error_code') == 18:
                raise MyExcept
        flag = 0
    except MyExcept:
        flag = 1
        print('Страница удалена или заблокирована\n')
    return flag


def get_request_for_get_user_id(user_input, token):
    params = get_params(token)
    params['user_ids'] = user_input
    response = requests.get(
        'https://api.vk.com/method/users.get',
        params=params
    )
    return response


def get_users_params(id_user, token):
    params = get_params(token)
    params['user_ids'] = id_user
    params['fields'] = ['books, can_see_audio, city, games, movies, music, sex, bdate']
    response = requests.get(
        'https://api.vk.com/method/users.get',
        params=params
    )
    return response


def search_list_users(token):
    params = get_params(token)
    params['hometown'] = 'Москва'
    params['sex'] = '1'
    params['status'] = '6'
    params['age_from'] = '24'
    params['age_to'] = '30'
    params['has_photo'] = '1'
    params['count'] = 1000
    params['fields'] = ['books, can_see_audio, city, games, movies, music, sex, bdate']
    # params['group_id'] = '1'
    response = requests.get(
        'https://api.vk.com/method/users.search',
        params=params
    )
    return response


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
