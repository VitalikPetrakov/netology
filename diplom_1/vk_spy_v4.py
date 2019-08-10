import requests
import time
import json

token = ''


def get_params():
    params = {
        'v': '5.101',
        'access_token': token,
    }
    return params


def get_request_for_get_user_id(metod, user_input):
    params = get_params()
    params['user_ids'] = user_input
    response = requests.get(
        'https://api.vk.com/method/' + metod,
        params=params
    )
    return response


def get_request_for_get_list_of_friends(metod, id_user):
    params = get_params()
    params['user_id'] = id_user
    response = requests.get(
        'https://api.vk.com/method/' + metod,
        params=params
    )
    return response


def get_request_for_get_list_of_id_groups(metod, id_user):
    params = get_params()
    params['user_id'] = id_user
    params['extended'] = '1',
    params['fields'] = 'members_count',
    params['count'] = '1000'
    response = requests.get(
        'https://api.vk.com/method/' + metod,
        params=params
    )
    return response


def get_request_for_get_info_general_groups(metod, id_group):
    params = get_params()
    params['group_id'] = id_group
    params['fields'] = 'members_count',
    response = requests.get(
        'https://api.vk.com/method/' + metod,
        params=params
    )
    return response


def get_user_id(user_input):
    response = get_request_for_get_user_id('users.get', user_input)
    user_id = (response.json()['response'][0]['id'])
    return user_id


def get_list_of_friends(id_user):
    response = get_request_for_get_list_of_friends('friends.get', id_user)
    list_user_friends = (response.json()['response']['items'])
    return list_user_friends


def get_list_of_id_groups(id_user):
    try:
        response = get_request_for_get_list_of_id_groups('groups.get', id_user)
        list_user_groups = (response.json()['response']['items'])
    except:
        time.sleep(1)
        response = get_request_for_get_list_of_id_groups('groups.get', id_user)
        list_user_groups = (response.json()['response']['items'])
    return list_user_groups


def get_set_of_id_friends_groups(user_id):
    set_id_friends_groups = set()
    list_user_friends = get_list_of_friends(user_id)
    i = 1
    print(f'Колличество друзей у пользователя: {len(list_user_friends)}')
    for friend in list_user_friends:
        try:
            list_user_groups = get_list_of_id_groups(friend)
            for group in list_user_groups:
                set_id_friends_groups.add(int(group['id']))
            print(f'Подсчет групп у пользователя под номером {i} из {len(list_user_friends)}')
            i += 1
            print('----------')
        except:
            print(f'Проблема со страницей у пользователя под номером {i} (страница закрыта или удалена)')
            print('----------')
            i += 1
            continue
    print(f'Общее колличество групп у друзей пользователя: {len(set_id_friends_groups)}')
    print('----------')
    return set_id_friends_groups


def get_set_of_id_user_groups(user_id):
    set_id_user_groups = set()
    list_of_groups = get_list_of_id_groups(user_id)
    for group in list_of_groups:
        set_id_user_groups.add(int(group['id']))
    return set_id_user_groups


def get_general_groups(user_id):
    list_general_groups = list()
    general_groups = get_set_of_id_user_groups(user_id) - get_set_of_id_friends_groups(user_id)
    list_general_groups.extend(list(general_groups))
    return list_general_groups


def get_info_general_groups(list_general_groups):
    groups_info = list()
    i = 1
    for id_group in list_general_groups:
        dict_group = dict()
        try:
            response = get_request_for_get_info_general_groups('groups.getById', id_group)
            test = response.json()['response'][0]['name']
        except:
            time.sleep(2)
            response = get_request_for_get_info_general_groups('groups.getById', id_group)
        print(f'Идет обработка информации группы с индификатором {id_group} ({i}/{len(list_general_groups)})')
        try:
            dict_group['name'] = response.json()['response'][0]['name']
            dict_group['gid'] = response.json()['response'][0]['id']
            dict_group['members_count'] = response.json()['response'][0]['members_count']
            print('----------')
            i += 1
        except:
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
    user_input = input('Введите ID профиля или его имя: ')
    if user_input.isdigit():
        user_id = user_input
    else:
        user_id = get_user_id(user_input)
    general_groups = get_general_groups(user_id)
    groups_info = get_info_general_groups(general_groups)
    set_of_id_user_groups = get_set_of_id_user_groups(user_id)
    print(f'Колличество групп, в которых нет друзей пользователя: {len(general_groups)}')
    print(f'Общее колличество групп у пользователя: {len(set_of_id_user_groups)}')
    write_json_file(groups_info)


if __name__ == '__main__':
    main()
