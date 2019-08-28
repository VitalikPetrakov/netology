"""
Ваша задача: починить адресную книгу, используя регулярные выражения.
Структура данных будет всегда:
lastname,firstname,surname,organization,position,phone,email
Предполагается, что телефон и e-mail у человека может быть только один.
Необходимо:

поместить Фамилию, Имя и Отчество человека в поля lastname, firstname и surname соответственно. В записной книжке
изначально может быть Ф + ИО, ФИО, а может быть сразу правильно: Ф+И+О;
привести все телефоны в формат +7(999)999-99-99. Если есть добавочный номер, формат будет такой: +7(999)999-99-99
 доб.9999;
объединить все дублирующиеся записи о человеке в одну.
"""


from pprint import pprint
# читаем адресную книгу в формате CSV в список contacts_list
import csv
with open('phonebook_raw.csv', 'rt', encoding='utf8') as file:
    rows = csv.reader(file, delimiter=",")
    contacts_list = list(rows)
    contacts_list = contacts_list[1:]
# pprint(contacts_list, width=300, depth=2)

# # TODO 1: выполните пункты 1-3 ДЗ








# TODO 2: сохраните получившиеся данные в другой файл
# код для записи файла в формате CSV
# with open("phonebook.csv", "w") as f:
#     datawriter = csv.writer(f, delimiter=',')
#   # Вместо contacts_list подставьте свой список
#     datawriter.writerows(contacts_list)



# def rebuild_names(unrebuild_data, index_in_data):
#     my_contact_list = []
#     for contact in unrebuild_data:
#         print(contact)
#         data = contact[index_in_data].split()
#         if len(contact[index_in_data].split()) == 1:
#             pass
#         elif len(contact[index_in_data].split()) == 2:
#             contact = contact[2:]
#             contact.insert(index_in_data, data[0])
#             # print(contact)
#             contact.insert(index_in_data + 1, data[1])
#             # print(contact)
#         elif len(contact[index_in_data].split()) == 3:
#             contact = contact[3:]
#             # print(contact)
#             contact.insert(index_in_data, data[0])
#             # print(contact)
#             contact.insert(index_in_data + 1, data[1])
#             # print(contact)
#             contact.insert(index_in_data + 2, data[2])
#             # print(contact)
#         my_contact_list.append(contact)
#     return my_contact_list
#
#
# pprint(rebuild_names(contacts_list, 0), width=300, depth=2)