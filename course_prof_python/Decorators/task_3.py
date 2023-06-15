from functools import wraps
from datetime import datetime


def logger(old_function):

    @wraps(old_function)
    def new_function(*args, **kwargs):

        start = datetime.now()

        result = old_function(*args, **kwargs)

        logs_row = f'start: {start}, func_name: {old_function.__name__}, args: {args}, ' \
                   f'kwargs: {kwargs}, result: {result}.\n'

        path = 'task_3.log'

        with open(path, 'a') as log_file:
            log_file.write(logs_row)

        return result

    return new_function


class FlatIterator:

    def __init__(self, list_of_list):
        self.list_of_list = list_of_list

    def __iter__(self):

        self.main_index = 0
        self.sub_index = -1
        return self

    @logger
    def __next__(self):
        self.sub_index += 1

        if self.sub_index == len(self.list_of_list[self.main_index]) and self.main_index < len(self.list_of_list):
            self.main_index += 1
            self.sub_index = 0

        if self.main_index == len(self.list_of_list):
            raise StopIteration

        item = self.list_of_list[self.main_index][self.sub_index]

        return item


if __name__ == '__main__':

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    result = FlatIterator(list_of_lists_1)

    print(*result, sep=', ', end='.')


