def selection_sort(lst: [int]) -> [int]:
    list_length = len(lst)
    for i in range(list_length):
        current_minimum_index = -1
        current_minimum_value = float('inf')
        for j in range(i, list_length):
            if lst[j] < current_minimum_value:
                current_minimum_index = j
                current_minimum_value = lst[j]
        if current_minimum_index != -1:
            lst[i], lst[current_minimum_index] = lst[current_minimum_index], lst[i]
    return lst


def test_selection_sort():
    assert selection_sort([]) == []
    assert selection_sort([1]) == [1]
    assert selection_sort([1, 2, 3, 4]) == [1, 2, 3, 4]
    assert selection_sort([4, 3, 2, 1]) == [1, 2, 3, 4]
    assert selection_sort([1, 2, 1, 2]) == [1, 1, 2, 2]
    assert selection_sort([2, 2, 2, 2, 2]) == [2, 2, 2, 2, 2]
    assert selection_sort([1, 1, 2, 2, 2]) == [1, 1, 2, 2, 2]
    assert selection_sort([21, 1, 27, 30, 12, 17]) == [1, 12, 17, 21, 27, 30]
