class Contact:

    def __init__(self, name, surname, tel, chosen=False, **kwargs):
        self.__name = name
        self.__surname = surname
        self.__tel = tel
        self.__kwargs = kwargs
        self.__chosen = chosen

    def __str__(self):
        data = f'''
Имя: {self.__name}
Фамилия: {self.__surname}
Телефон: {self.__tel}
В избранных: {'да' if self.__chosen else 'нет'}'''
        if self.__kwargs:
            data += '\nДополнительная информация:'
        for key, value in self.__kwargs.items():
            data += f'\n\t{key} : {value}'
        return data

    def get_tel(self):
        return self.__tel

    def get_chosen(self):
        return self.__chosen

    def get_name(self):
        return self.__name

    def get_surname(self):
        return self.__surname


class PhoneBook:

    def __init__(self, name):
        self.__name = name
        self.__contact_list = []

    def add_new_contact(self, contact):
        self.__contact_list.append(contact)

    def print_contact_list(self):
        for contact in self.__contact_list:
            print(contact)

    def del_contact_by_tel(self, tel):
        for contact in self.__contact_list:
            if tel == contact.get_tel():
                self.__contact_list.remove(contact)

    def search_chosen_one(self):
        for contact in self.__contact_list:
            if contact.get_chosen() is False:
                self.__contact_list.remove(contact)

    def search_by_name_and_surname(self, name, surname):
        for contact in self.__contact_list:
            if name == contact.get_name() and surname == contact.get_surname():
                print(contact)


if __name__ == '__main__':
    jhon = Contact('Jhon', 'Smith', '+71234567809', chosen=True, telegram='@jhony', email='jhony@smith.com')
    petet = Contact('Peter', 'Test', '+79876543210', chosen=False, telegram='@peter',
                    watsapp='Peter123', email='peter@gmail.com')
    petet1 = Contact('Peter1', 'Test1', '+798765432101', chosen=True, telegram='@peter1',
                     watsapp='Peter1231', email='peter@gmail.com1')
    print(jhon)
    my_phonebook = PhoneBook('Book')
    my_phonebook.add_new_contact(jhon)
    my_phonebook.add_new_contact(petet)
    my_phonebook.add_new_contact(petet1)
    my_phonebook.print_contact_list()
    # my_phonebook.del_contact_by_tel('+7987654321')
    # my_phonebook.search_chosen_one()
    # my_phonebook.search_by_name_and_surname('Peter', 'Test')
