import re
from pprint import pprint
import csv


with open('phonebook_raw.csv', 'rt', encoding='utf8') as file:
    rows = csv.reader(file)
    contacts_list = list(rows)
    headers = contacts_list[0]
    contacts_list = contacts_list[1:]


def work_with_name_and_tel(contacts_list):
    my_contact_list = []
    for contact in contacts_list:
        fio_str = ' '.join(contact[:2])
        fio_str = re.sub("[\s]+", " ", fio_str)
        fio_list = re.split(" ", fio_str)
        while len(fio_list) < 3:
            fio_list.append('')
        pattern_big_tel = re.compile("(\+7|8).*?(\d{3}).*?(\d{3}).*?(\d{2}).*?"
                                 "(\d{2}).*?(\(|\s|^\s).*?(\w+.).*?(\d+)(\)|$)")
        pattern_small_tel = re.compile("(\+7|8).*?(\d{3}).*?(\d{3}).*?(\d{2}).*?(\d{2})")
        if 'доб' in contact[5]:
            write_tel = pattern_big_tel.sub(r"+7(\2)\3-\4-\5 \7\8", contact[5])
        else:
            write_tel = pattern_small_tel.sub(r"+7(\2)\3-\4-\5", contact[5])
        contact.pop(5)
        contact.insert(5, write_tel)
        my_str = fio_list[:3]+contact[3:]
        my_contact_list.append(my_str)
    return my_contact_list


def del_repeat(contacts_list):
    n = 0
    my_dict = {}
    list_uncopy_contacts = []
    new_contacts_list = []
    for contact in contacts_list:

        if contact[0] not in my_dict.keys():
            my_dict.setdefault(contact[0], list())
            my_dict[contact[0]].append(n)
            n += 1
        else:
            my_dict[contact[0]].append(n)
            n += 1
    for key, item in my_dict.items():
        if len(item) > 1:
            resalt = []
            n = 0
            for i in contacts_list[item[0]]:
                if i:
                    resalt.append(i)
                    n += 1
                else:
                    resalt.append(contacts_list[item[1]][n])
                    n += 1
            new_contacts_list.append(resalt)
        else:
            for i in item:
                list_uncopy_contacts.append(i)
    for i in list_uncopy_contacts:
        new_contacts_list.append(contacts_list[i])
    return new_contacts_list


if __name__ == '__main__':
    contacts_list = work_with_name_and_tel(contacts_list)
    contacts_list = (del_repeat(contacts_list))
    contacts_list.insert(0, headers)
    pprint(contacts_list, width=300, depth=2)
    with open("phonebook.csv", "w") as f:
        datawriter = csv.writer(f, delimiter=',')
        datawriter.writerows(contacts_list)


