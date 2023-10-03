class FlatIterator:
    def __init__(self, list_of_lists):
        self.list_of_lists = list_of_lists
        self.current_list_index = 0
        self.current_element_index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_list_index >= len(self.list_of_lists):
            raise StopIteration

        current_list = self.list_of_lists[self.current_list_index]

        if self.current_element_index >= len(current_list):
            self.current_list_index += 1
            self.current_element_index = 0
            return next(self)

        item = current_list[self.current_element_index]
        self.current_element_index += 1
        return item


def test_1():
    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):
        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]


def print_flat_representation(list_of_lists):
    for flat_iterator_item in FlatIterator(list_of_lists):
        print(f"item = {flat_iterator_item}")


if __name__ == '__main__':
    test_1()
    list_of_lists_2 = [
        [1, 2, 3],
        ['d', 'e', 'f', 'h', False],
        ['a', 'b', None]
    ]

    print_flat_representation(list_of_lists_2)
