def len_sort(_files_dict):
    result = {}
    work_dict = {}
    for _file_name in _files_dict:
        with open(_file_name) as f:
            work_dict[_file_name] = len(f.readlines())
    for _key, _value in sorted(work_dict.items(), key=lambda p: p[1]):
        result[_key] = _value
    return result


def all_to_one(new_file_name):
    _files_dict = len_sort(files_dict)
    for _file_name in _files_dict:
        with open(new_file_name, 'a') as new_f:
            with open(_file_name) as current_file:
                new_f.write(f'{_file_name}\n{_files_dict[_file_name]}\n')
                for line in current_file.readlines():
                    new_f.write(line)
    return


files_dict = {'1.txt': None, '2.txt': None, '3.txt': None}

# Вызываем функцию, указывая в качестве аргумента желаемое имя сводного файла.
all_to_one('123.txt')

