
file_name = "recipes.txt"

# Задача 1:

from pprint import pprint
#
def cook_book(file_name):
    with open(file_name, 'r', encoding='utf-8') as file:
        cook_book = {}
        for line in file:
            dish_name = line.strip()
            cook_book[dish_name] = []
            for i in range(int(file.readline())):
                composition = file.readline().split(' | ')
                cook_book[dish_name].append({'ingredient_name': composition[0],
                                             'quantity': int(composition[1]),
                                             'measure': composition[2].strip()})
            file.readline()
    return cook_book

pprint(cook_book(file_name))

# Задача 2

def get_shop_list_by_dishes(dishes, cook_book, person_count):
    result = {}
    for dish in dishes:
        if dish in cook_book:
            for composition in cook_book[dish]:
                if composition['ingredient_name'] in result:
                    result[composition['ingredient_name']]['quantity'] += composition['quantity'] * person_count
                else:
                    result[composition['ingredient_name']] = {'measure': composition['measure'],
                                                              'quantity': (composition['quantity'] * person_count)}
        else:
            print(f'Рецепт для "{dish}" отсутствует в кулинарной книге')
    return result

pprint(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], cook_book('recipes.txt'), 2))

