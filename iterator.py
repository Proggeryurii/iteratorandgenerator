class FlatIterator:

    def __init__(self, list_of_lists):
        self.list_of_lists = list_of_lists
        self.outer_index = 0
        self.inner_index = 0

    def __iter__(self):
        return self

    def __next__(self):
        # Проверяем, достиг ли outer_index конца списка списков
        if self.outer_index >= len(self.list_of_lists):
            raise StopIteration

        # Если inner_index выходит за пределы текущего внутреннего списка, переходим к следующему внутреннему списку
        while self.inner_index >= len(self.list_of_lists[self.outer_index]):
            self.outer_index += 1
            self.inner_index = 0
            # Если после увеличения outer_index он выходит за пределы списка списков, останавливаем итерацию
            if self.outer_index >= len(self.list_of_lists):
                raise StopIteration

        item = self.list_of_lists[self.outer_index][self.inner_index]
        self.inner_index += 1
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


if __name__ == '__main__':
    test_1()