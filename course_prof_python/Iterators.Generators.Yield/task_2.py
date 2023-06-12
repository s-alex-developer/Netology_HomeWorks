import types


def flat_generator(list_of_lists):
    list_of_lists_index = 0
    list_index = -1
    while list_of_lists_index < len(list_of_lists):

        while list_index < len(list_of_lists[list_of_lists_index])-1:
            list_index += 1
            yield list_of_lists[list_of_lists_index][list_index]

        list_index = -1
        list_of_lists_index += 1


def test_2():
    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            flat_generator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):
        assert flat_iterator_item == check_item

    assert list(flat_generator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]

    assert isinstance(flat_generator(list_of_lists_1), types.GeneratorType)


if __name__ == '__main__':
    test_2()
