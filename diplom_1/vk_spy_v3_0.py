import requests
import time
import json

token = ''

def get_user_id(user_input):
    response = requests.get(
        'https://api.vk.com/method/users.get',
        params={
            'access_token': token,
            'v': '5.101',
            'user_ids': user_input,
        }
    )
    user_id = (response.json()['response'][0]['id'])
    return user_id


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
    try:
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
    except:
        time.sleep(1)
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
            print(f'Проблема со страницей у пользователя под номером (страница закрыта или удалена) {i}')
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
            response = requests.get(
                'https://api.vk.com/method/groups.getById',
                params={
                    'access_token': token,
                    'v': '5.101',
                    'group_id': id_group,
                    'fields': 'members_count',
                }
            )
            test = response.json()['response'][0]['name']
        except:
            time.sleep(2)
            response = requests.get(
                'https://api.vk.com/method/groups.getById',
                params={
                    'access_token': token,
                    'v': '5.101',
                    'group_id': id_group,
                    'fields': 'members_count',
                }
            )
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
    set_of_id_user_groups = get_set_of_id_user_groups(user_id)
    groups_info = get_info_general_groups(general_groups)
    print(f'Колличество групп, в которых нет друзей пользователя: {len(general_groups)}')
    print(f'Общее колличество групп у пользователя: {len(set_of_id_user_groups)}')
    write_json_file(groups_info)


if __name__ == '__main__':
    main()
