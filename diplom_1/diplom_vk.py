import requests
import time
import json


class MyExcept(Exception):
    pass


def check_user(user_id, token):
    try:
        response = get_request_for_get_list_of_id_groups('groups.get', user_id, token)
        my_response = response.json()
        if 'error' in my_response.keys():
            if my_response.get('error').get('error_code') == 18:
                raise MyExcept
        flag = 0
    except MyExcept:
        flag = 1
        print('Страница удалени или заблокирована\n')
    return flag


def get_params(token):
    params = {
        'v': '5.101',
        'access_token': token,
    }
    return params


def get_request_for_get_user_id(metod, user_input, token):
    params = get_params(token)
    params['user_ids'] = user_input
    response = requests.get(
        'https://api.vk.com/method/' + metod,
        params=params
    )
    return response


def get_request_for_get_list_of_friends(metod, id_user, token):
    params = get_params(token)
    params['user_id'] = id_user
    response = requests.get(
        'https://api.vk.com/method/' + metod,
        params=params
    )
    return response


def get_request_for_get_list_of_id_groups(metod, id_user, token):
    params = get_params(token)
    params['user_id'] = id_user
    params['extended'] = '1',
    params['fields'] = 'members_count',
    params['count'] = '1000'
    response = requests.get(
        'https://api.vk.com/method/' + metod,
        params=params
    )
    return response


def get_request_for_get_info_general_groups(metod, id_group, token):
    params = get_params(token)
    params['group_id'] = id_group
    params['fields'] = 'members_count',
    response = requests.get(
        'https://api.vk.com/method/' + metod,
        params=params
    )
    return response


def get_user_id(user_input, token):
    try:
        response = get_request_for_get_user_id('users.get', user_input, token)
        user_id = (response.json()['response'][0]['id'])
    except KeyError:
        print('Данного прользователя не существует\n')
        user_id = '-1'
    except IndexError:
        print('Не был введен пользователь')
        user_id = '-1'
    return user_id


def get_list_of_friends(id_user, token):
    response = get_request_for_get_list_of_friends('friends.get', id_user, token)
    list_user_friends = (response.json()['response']['items'])
    return list_user_friends


def get_list_of_id_groups(id_user, token):
    try:
        response = get_request_for_get_list_of_id_groups('groups.get', id_user, token)
        my_response = response.json()
        if 'error' in my_response.keys():
            if my_response.get('error').get('error_code') == 6:
                raise MyExcept('To many requests')
        list_user_groups = (response.json()['response']['items'])
    except MyExcept:
        print('Слишком много запросов, ждем 2 секунды перед повторным запросом')
        print('----------')
        time.sleep(2)
        response = get_request_for_get_list_of_id_groups('groups.get', id_user, token)
        list_user_groups = (response.json()['response']['items'])
    return list_user_groups


def get_set_of_id_friends_groups(user_id, token):
    set_id_friends_groups = set()
    list_user_friends = get_list_of_friends(user_id, token)
    i = 1
    print(f'Колличество друзей у пользователя: {len(list_user_friends)}')
    for friend in list_user_friends:
        try:
            list_user_groups = get_list_of_id_groups(friend, token)
            for group in list_user_groups:
                if int(group['id']) is False:
                    raise KeyError
                set_id_friends_groups.add(int(group['id']))
            print(f'Подсчет групп у пользователя под номером {i} из {len(list_user_friends)} id{friend}')
            i += 1
            print('----------')
        except KeyError:
            print(f'Проблема со страницей у пользователя под номером {i} id{friend} (страница закрыта или удалена)')
            print('----------')
            i += 1
    print(f'Общее колличество групп у друзей пользователя: {len(set_id_friends_groups)}')
    print('----------')
    return set_id_friends_groups


def get_set_of_id_user_groups(user_id, token):
    set_id_user_groups = set()
    list_of_groups = get_list_of_id_groups(user_id, token)
    for group in list_of_groups:
        set_id_user_groups.add(int(group['id']))
    return set_id_user_groups


def get_general_groups(user_id, token):
    list_general_groups = list()
    general_groups = get_set_of_id_user_groups(user_id, token) - get_set_of_id_friends_groups(user_id, token)
    list_general_groups.extend(list(general_groups))
    return list_general_groups


def get_info_general_groups(list_general_groups, token):
    groups_info = list()
    i = 1
    for id_group in list_general_groups:
        dict_group = dict()
        try:
            response = get_request_for_get_info_general_groups('groups.getById', id_group, token)
            my_response = response.json()
            if 'error' in my_response.keys():
                if my_response.get('error').get('error_code') == 6:
                    raise MyExcept('To many requests')
        except MyExcept:
            print('Слишком много запросов, ждем 2 секунды перед повторным запросом')
            print('----------')
            time.sleep(2)
            response = get_request_for_get_info_general_groups('groups.getById', id_group, token)
        print(f'Идет обработка информации группы с индификатором {id_group} ({i}/{len(list_general_groups)})')
        try:
            dict_group['name'] = response.json()['response'][0]['name']
            dict_group['gid'] = response.json()['response'][0]['id']
            if 'members_count' not in response.json()['response'][0]:
                raise MyExcept
            dict_group['members_count'] = response.json()['response'][0]['members_count']
            print('----------')
            i += 1
        except MyExcept:
            print('----------')
            print(f'Информацию группе {id_group} получить не получилось (группа приватная или удалена)')
            print('----------')
            i += 1
            continue
        groups_info.append(dict_group)
    return groups_info


def write_json_file(groups_info):
    data = groups_info
    with open('groups.json', 'wt', encoding='utf8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)


def main():
    token = '03f14ae5b74728e76d72eaa8088bc91eec376ef021a907e861af21364655e7742a5510fe59f3384a97169'
    while True:
        user_input = input('Введите ID профиля или его имя (0 - выход из программы): ')
        if user_input != '0':
            if user_input.isdigit():
                user_id = user_input
                flag = check_user(user_id, token)
                if flag == 0:
                    general_groups = get_general_groups(user_id, token)
                    groups_info = get_info_general_groups(general_groups, token)
                    set_of_id_user_groups = get_set_of_id_user_groups(user_id, token)
                    print(f'Колличество групп, в которых нет друзей пользователя: {len(general_groups)}')
                    print(f'Общее колличество групп у пользователя: {len(set_of_id_user_groups)}')
                    write_json_file(groups_info)
                    print('\n')
                else:
                    continue
            else:
                user_id = get_user_id(user_input, token)
                if user_id == '-1':
                    continue
                else:
                    general_groups = get_general_groups(user_id, token)
                    groups_info = get_info_general_groups(general_groups, token)
                    set_of_id_user_groups = get_set_of_id_user_groups(user_id, token)
                    print(f'Колличество групп, в которых нет друзей пользователя: {len(general_groups)}')
                    print(f'Общее колличество групп у пользователя: {len(set_of_id_user_groups)}')
                    write_json_file(groups_info)
                    print('\n')

        else:
            print('Конец программы!')
            break


if __name__ == '__main__':
    main()
