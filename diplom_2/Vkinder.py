'''TODO
Дипломная работа
VKinder


Используя данные из VK нужно сделать сервис намного лучше чем Tinder.
 Искать людей, подходящих под условия, на основании информации о пользователе из VK:

диапазон возраста,
пол,
группы,
расположение,
интересы,
любой другой необязательный параметр.

У каждого критерия поиска должны быть свои веса. То есть совпадение по возрасту должны быть важнее общих групп.
Интересы по музыке важнее книг. Наличие общих друзей важнее возраста.
Разбор похожих интересов(книги, музыка, интересы) нужно будет провести с помощью анализа текста.
У тех людей, которые подошли по требованиям пользователю, получать топ-3 популярных фотографии с аватара.
Популярность определяется по количеству лайков.
Входные данные
Имя пользователя или его id в ВК, для которого мы ищем пару.
если информации недостаточно нужно дополнительно спросить её у пользователя.
Выходные данные
JSON-файл с 10 объектами, где у каждого объекта перечислены топ-3 фотографии и ссылка на аккаунт.
Требование к сервису:
Код программы удовлетворяетPEP8.
'https://requests-oauthlib.readthedocs.io/en/latest/oauth2_workflow.html'
Получать токен от пользователя с нужными правами.
Программа декомпозирована на функции/классы/модули/пакеты.
Результат программы записывать в БД.
Люди не должны повторяться при повторном поиске.
Реализовать тесты на базовую функциональность.
Не запрещается использовать внешние библиотеки для vk.'''
import diplom_2.database
import datetime
from diplom_2.my_requests import check_user, search_list_users, get_users_params, get_user_id, \
    get_request_for_get_user_id, get_id_from_name, check_id_and_name_equal
from pprint import pprint


token = '9536a934fa0dbfdeaed31db8a021e1bc8848c737fe945292f68cf7da903e8f65fa7010e2d4b80bb30e993'


if __name__ == '__main__':
    while True:
        user_input = input('Введите ID профиля или его имя (0 - выход из программы): ')
        if user_input != '0':
            if user_input.isdigit():
                user_id = user_input
                flag = check_user(user_id, token)

    # response_list_need_users = search_list_users(token)
    # list_need_users = response_list_need_users.json()['response']['items']
    # pprint.pprint(list_need_users)

    # check_user(get_id_from_name('Иван Иванов', token), 'Иван Иванов', token)
    # pprint(get_request_for_get_user_id('1', token).json())
    # check_id_and_name_equal('Дуров Павел', 1, token)