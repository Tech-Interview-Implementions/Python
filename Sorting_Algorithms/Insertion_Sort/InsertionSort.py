def insertion_sort(lst: [int]) -> [int]:
    for i in range(len(lst)):
        j = i
        while j > 0 and lst[j-1] > lst[j]:
            lst[j-1], lst[j] = lst[j], lst[j-1]
            j -= 1

    return lst


def test_insertion_sort():
    assert insertion_sort([]) == []
    assert insertion_sort([1]) == [1]
    assert insertion_sort([1, 2, 3, 4]) == [1, 2, 3, 4]
    assert insertion_sort([4, 3, 2, 1]) == [1, 2, 3, 4]
    assert insertion_sort([1, 2, 1, 2]) == [1, 1, 2, 2]
    assert insertion_sort([1, 1, 2, 2, 2]) == [1, 1, 2, 2, 2]
    assert insertion_sort(
        [21, 1, 27, 30, 12, 17, 20, 28, 16, 4, 11, 5, 8, 2, 38, 26, 10, 25, 23]
    ) == [1, 2, 4, 5, 8, 10, 11, 12, 16, 17, 20, 21, 23, 25, 26, 27, 28, 30, 38]
