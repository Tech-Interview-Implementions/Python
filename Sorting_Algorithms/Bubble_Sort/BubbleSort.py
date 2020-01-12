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
