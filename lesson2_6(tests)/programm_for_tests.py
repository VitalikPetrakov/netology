documents = [
    {'type': 'passport', 'number': '2207 876234', 'name': 'Василий Гупкин'},
    {'type': 'invoice', 'number': '11-2', 'name': 'Геннадий Покемонов'},
    {'type': 'insurance', 'number': '10006', 'name': 'Аристарх Павлов'}
]

directories = {
    '1': ['2207 876234', '11-2'],
    '2': ['10006'],
    '3': []
}


def find_people(documents):
    doc_num = input('Введите норме документа: ')
    flag = 0
    for document in documents:
        if doc_num == document['number']:
            print(document['name'])
            flag = 1
    if flag == 0:
        print('Введен несуществующий документ')


def documents_in_list(documents):
    for document in documents:
        type_of_doc = document['type']
        num_of_doc = document['number']
        peolple_doc = document['name']
        print(f'{type_of_doc} "{num_of_doc}" "{peolple_doc}"')


def get_shelf(directories):
    value_directory = input(str('Введите норме документа: '))
    flag = 0
    for num_shelf, num_doc in directories.items():
        for num in num_doc:
            if value_directory == num:
                print(num_shelf)
                flag = 1
    if flag == 0:
        print('Введен несуществующий номер документа')


def add_new_doc(documents, directories):
    type_new_doc = input(str('Введите тип нового документа: '))
    num_new_doc = input(str('Введите номер нового документа: '))
    man_new_doc = input(str('Введите имя, чей документ добавляется: '))
    shelf_new_doc = input('Введите номер полки для нового документа: ')
    new_dict = {'type': type_new_doc, 'number': num_new_doc, 'name': man_new_doc}
    if shelf_new_doc in directories.keys():
        directories[shelf_new_doc].append(num_new_doc)
        print(directories)
        documents.append(new_dict)
        print(documents)
    else:
        print('Введен номер несуществующей полки')
        new_shelf = input('Добавить новую полку? Введите Y/N: ')
        if new_shelf == 'Y':
            directories.setdefault(shelf_new_doc, list())
            directories[shelf_new_doc].append(num_new_doc)
            print(directories)
            documents.append(new_dict)
            print(documents)
        else:
            print('Документ не был добавлен')


def del_doc_by_num(documents):
    num_doc_to_del = input(str('Введите номер документа для удаления: '))
    flag = 0
    for document in documents:
        if num_doc_to_del == document['number']:
            flag = 1
            documents.remove(document)
    if flag == 0:
        print('Введен несуществующий номер документа')
    else:
        for num_shelf, num_doc in directories.items():
            for num in num_doc:
                if num_doc_to_del == num:
                    num_doc.remove(num_doc_to_del)
        print(documents)
        print(directories)


def move_from_shelf_to_shelf(directories):
    num_doc_to_move = input(str('Введите номер документа для переноса: '))
    flag_num_shelf = 0
    for num_shelf, num_doc in directories.items():
        for num in num_doc:
            if num_doc_to_move == num:
                flag_num_shelf = 1
    if flag_num_shelf == 0:
        print('Введен несуществующий документ')
    else:
        num_shelf_to_move = input('Введите номер целевой полки: ')
        if num_shelf_to_move in directories.keys():
            for num_shelf, num_doc in directories.items():
                for num in num_doc:
                    if num_doc_to_move == num:
                        num_doc.remove(num_doc_to_move)
            directories[num_shelf_to_move].append(num_doc_to_move)
            print(directories)
        else:
            print('Введен номер несуществующей полки')
            new_shelf = input('Добавить новую полку? Введите Y/N: ')
            if new_shelf == 'Y':
                directories.setdefault(num_shelf_to_move, list())
                for num_shelf, num_doc in directories.items():
                    for num in num_doc:
                        if num_doc_to_move == num:
                            num_doc.remove(num_doc_to_move)
                directories[num_shelf_to_move].append(num_doc_to_move)
                print(directories)
            else:
                print('Документ не был перенесен')


def add_new_shelf(directories):
    new_shelf = input(str('Введине номер новой полки: '))
    directories.setdefault(new_shelf, list())
    print(directories)


def main():
    while True:
        user_input = input('''
Для выбора комманды введите ее краткое обозначение: 
p – команда для поиска человека по номеру документа;
l – команда для вывода всех сохранненных документов;
s – команда для поиска номера полки по номеру документа;
a – команда для добавления нового документа;
d – команда для удаления документа по номеру;
q - завершение работы программы;
m – команда для переноса нужного документа на новую полку;
as – команда для добавления новой полки в перечень;
            \n:''')
        if user_input == 'p':
            find_people(documents)
        elif user_input == 'l':
            documents_in_list(documents)
        elif user_input == 's':
            get_shelf(directories)
        elif user_input == 'a':
            add_new_doc(documents, directories)
        elif user_input == 'd':
            del_doc_by_num(documents)
        elif user_input == 'm':
            move_from_shelf_to_shelf(directories)
        elif user_input == 'as':
            add_new_shelf(directories)
        elif user_input not in ['p', 'l', 's', 'a', 'q', 'd', 'm', 'as']:
            print('Введена неверная коммандв')
        elif user_input == 'q':
            break

if __name__ == main():
    main()