import re
import csv

if __name__ == "__main__":

    # Читаем адресную книгу в формате CSV в список contacts_list:

    with open("phonebook_raw(without_mistake).csv") as f:
        rows = csv.reader(f, delimiter=",")
        contacts_list = list(rows)

    # 1. Выполните пункты 1-3 задания.
    # Ваш код

    first_row = contacts_list.pop(0)

    work_str = ''

    for el in contacts_list:
        work_str += ','.join(el) + '\n'

    pattern = r'^([а-яёА-ЯЁ]*)([\s\,])([а-яёА-ЯЁ]*)([\s\,])([а-яёА-ЯЁ]*)(\,{1,3})([а-яёА-ЯЁ]*)(\,{1,2})' \
              r'([а-яёА-ЯЁ\s–]*)(\,)([+7|7|8]+)?([\s\(]+)?(\d{3})?([\s\)\-]+)?(\d{3})?(-)?(\d{2})?(-)?(\d{2})?' \
              r'([\s\,])?\(?(доб.\s\d{4})?([\),]+)?([\w\._-]*@[\w\._-]*)?'

    new_pattern = r'\1,\3,\5,\7,\9,+7(\13)\15-\17-\19 \21,\23'

    work_str = re.sub(pattern, new_pattern, work_str, flags=re.MULTILINE) \
        .replace(' ,', ',').replace('+7()--,', ',').replace('. ', '.')

    work_list = []

    for elem in work_str.split('\n'):

        work_list.append(elem.split(','))

    work_list = work_list[:-1]

    finally_list = []
    check_list = []
    start = 0

    for check_elem in work_list[:-1]:

        start += 1
        new_row = []
        position_index = 0

        for elem in work_list[start:]:

            if check_elem[0] == elem[0] and check_elem[1] == elem[1]:

                new_row.append(check_elem[0])
                new_row.append(check_elem[1])
                i = 2

                while i < len(check_elem):

                    if check_elem[i] == elem[i]:
                        new_row.append(check_elem[i])

                    if check_elem[i] != elem[i] and check_elem[i] != '':
                        new_row.append(check_elem[i])

                    if check_elem[i] != elem[i] and elem[i] != '':
                        new_row.append(elem[i])

                    i += 1
                finally_list.append(new_row)
                check_list.append(work_list[start + position_index])

                break
            position_index += 1

        else:
            if check_elem not in check_list:
                finally_list.append(check_elem)

    finally_list.insert(0, first_row)

    # 2. Сохраните получившиеся данные в другой файл.
    # Код для записи файла в формате CSV:
    with open("phonebook.csv", "w+", newline='') as f:
        datawriter = csv.writer(f, delimiter=',')

        # Вместо contacts_list подставьте свой список:
        datawriter.writerows(finally_list)
