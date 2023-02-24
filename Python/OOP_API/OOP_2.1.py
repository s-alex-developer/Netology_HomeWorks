from pprint import pprint

# Задача №1.
def file_to_dict():
    with open('recipes.txt') as f:
        cook_book = {}
        wl = []
        limit = len(f.readlines())
        count = 0
        f.seek(0)
        for el in f.readlines():
            count += 1
            if el != '\n':
                if '|' in el:
                    wl.append((el.replace('|', '').strip()).split('  '))
                else:
                    wl.append(el.strip())
            if el == '\n' or count == limit:
                cook_book[wl[0]] = []
                for _el in wl[2:]:
                    cook_book[wl[0]].append({'ingredient_name': _el[0],
                                             'quantity': int(_el[1]), 'measure': _el[2]})
                wl = []
                continue
    return cook_book


# Задача №2.
def get_shop_list_by_dishes(dishes, person_count):
    cook_book = file_to_dict()
    shop_list = {}
    for dish in dishes:
        for el in cook_book[dish]:
            if el['ingredient_name'] not in shop_list:
                shop_list[el['ingredient_name']] = {'measure': el['measure'],
                                                    'quantity': el['quantity'] * person_count}
            else:
                shop_list[el['ingredient_name']]['quantity'] += el['quantity'] * person_count
    return pprint(shop_list)


print('----- Задача №1 -----')
print()
pprint(file_to_dict())
print()
print('----- Задача №2 -----')
print()
get_shop_list_by_dishes(['Запеченный картофель', 'Омлет', 'Фахитос'], 1)
