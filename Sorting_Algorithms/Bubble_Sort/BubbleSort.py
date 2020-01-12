def bubble_sort(lst: [int]) -> [int]:
    """
    :param lst: List that is to be sorted
    :return: List that is sorted
    """

    list_length = len(lst)

    for i in range(list_length-1):
        for j in range(list_length-i-1):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]

    return lst


def test_bubble_sort():
    assert bubble_sort([]) == []
    assert bubble_sort([1]) == [1]
    assert bubble_sort([1, 2, 3, 4]) == [1, 2, 3, 4]
    assert bubble_sort([4, 3, 2, 1]) == [1, 2, 3, 4]
    assert bubble_sort([1, 2, 1, 2]) == [1, 1, 2, 2]
    assert bubble_sort([1, 1, 2, 2, 2]) == [1, 1, 2, 2, 2]
    assert bubble_sort(
        [21, 1, 27, 30, 12, 17, 20, 28, 16, 4, 11, 5, 8, 2, 38, 26, 10, 25, 23]
    ) == [1, 2, 4, 5, 8, 10, 11, 12, 16, 17, 20, 21, 23, 25, 26, 27, 28, 30, 38]
