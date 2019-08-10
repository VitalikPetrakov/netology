# ____________задание №1_________________
while True:
    user_input = str(input('Введите символы через пробел для вычисления: '))
    user_input_list = list(user_input.split())
    try:
        assert user_input_list[0] in ['+', '/', '*', '-']
        if user_input_list[0] == '+':
            print(int(user_input_list[1]) + int(user_input_list[2]))
        elif user_input_list[0] == '*':
            print(int(user_input_list[1]) * int(user_input_list[2]))
        elif user_input_list[0] == '-':
            print(int(user_input_list[1]) - int(user_input_list[2]))
        elif user_input_list[0] == '/':
            print(int(user_input_list[1]) / int(user_input_list[2]))
    except IndexError:
        print('Не хватает одного из аргументов')
    except AssertionError:
        print("Первый символ должен быть одним из '+','/','*','-'")
    except ZeroDivisionError:
        print('На ноль делить нельзя')
    except ValueError:
        print('Операции в программе можно выполнять только над цифрами')
    except BaseException:
        print('Непредвиденная ошибка')
    finally:
        print('Конец программы')


#___________зададие №2 варинт 1__________________

# def my_except(documents):
#     i = 1
#     for document in documents:
#         if 'name' not in document:
#             raise KeyError(f'В документе №{i} нет ключа "name"')
#         i += 1
#     print('все хорошо с документами')
#
#
# my_except(documents)


#___________зададие №2 варинт 2__________________

# def documents_in_list(documents):
#     i = 1
#     try:
#         for document in documents:
#             type_of_doc = document['type']
#             num_of_doc = document['number']
#             peolple_doc = document['name']
#             print(f'{type_of_doc} "{num_of_doc}" "{peolple_doc}"')
#             i += 1
#     except KeyError:
#         print((f'В документе №{i} нет ключа "name"'))
#     finally:
#         print('Конец программы')
#
#
# documents_in_list(documents)
