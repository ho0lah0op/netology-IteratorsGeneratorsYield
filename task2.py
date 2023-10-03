import types


def flat_generator(list_of_lists):
    for sublist in list_of_lists:
        for item in sublist:
            yield item


def test_2():
    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_generator_item, check_item in zip(
            flat_generator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):
        assert flat_generator_item == check_item

    assert list(flat_generator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]

    assert isinstance(flat_generator(list_of_lists_1), types.GeneratorType)


def print_flat_representation(list_of_lists):
    for item in flat_generator(list_of_lists_2):
        print(f"item = {item}")


if __name__ == '__main__':
    test_2()
    list_of_lists_2 = [
        [1, 2, 3],
        ['d', 'e', 'f', 'h', False],
        ['a', 'b', None]
    ]
    print_flat_representation(list_of_lists_2)

