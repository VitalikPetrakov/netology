from pprint import pprint


def append_new_dish(cook_book, recipes):
    name_of_dish = recipes.readline().strip()
    if name_of_dish:
        cook_book.setdefault(name_of_dish, list())
        value_ingredients = int(recipes.readline().strip())
        for line in range(value_ingredients):
            ingredient = {}
            ingredient_in_list = (recipes.readline().strip().split(' | '))
            ingredient['ingridient_name'] = ingredient_in_list[0]
            ingredient['quantity'] = ingredient_in_list[1]
            ingredient['measure'] = ingredient_in_list[2]
            cook_book[name_of_dish].append(ingredient)
        recipes.readline()
        return True
    else:
        return False


def get_shop_list_by_dishes(dishes, person_count, cook_book):
    shop_list = dict()
    for dish in dishes:
        one_dish = cook_book.get(dish)
        for ingredient in one_dish:
            if shop_list.get(ingredient['ingridient_name']) is None:
                shop_list[ingredient['ingridient_name']] = {'measure': ingredient['measure'], 'quantity': int(ingredient['quantity']) * person_count}
            else:
                shop_list[ingredient['ingridient_name']]['quantity'] += int(ingredient['quantity']) * person_count
    pprint(shop_list, depth=3, width=100)


def get_cook_book():
    cook_book = dict()
    with open('recipes.txt', encoding='utf-8') as recipes:
        while append_new_dish(cook_book, recipes):
            pass
        pprint(cook_book, depth=3, width=100)
        print()
    return cook_book


def __main__():
    list = input('Введите блюда для списка: ')
    my_list = list.split(' ')
    print(my_list)
    counter_people = int(input('Введите колличество людей: '))
    get_shop_list_by_dishes(my_list, counter_people, get_cook_book())


__main__()