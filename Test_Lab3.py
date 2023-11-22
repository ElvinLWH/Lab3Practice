import Lab3

print("Test_Lab3")


def test_bubble_sort_ascending():
    result = []
    input_arr = [64, 34, 25, 12, 22, 11, 90]
    test_arr = [11, 12, 22, 25, 34, 64, 90]

    result = Lab3.bubble_sort(input_arr, Lab3.SORT_ASCENDING)

    assert (result == test_arr)

def test_bubble_sort_descending():
    result = []
    input_arr = [64, 34, 25, 12, 22, 11, 90]
    test_arr = [90, 64, 34, 25, 22, 12, 11]

    result = Lab3.bubble_sort(input_arr, Lab3.SORT_DESCENDING)

    assert (result == test_arr)

def test_bubble_sort_invalid():
    result = []
    input_arr = [64, 34, 25, 12, 22, 11, 90]

    result = Lab3.bubble_sort(input_arr, 3)

    assert (result == [])

def test_greater_than_or_equal_to_ten():
    result = []
    input_arr = [12, 23, 45, 54, 67, 1, 3, 5, 6, 7]
    expected_result = 1

    result =Lab3.bubble_sort(input_arr, Lab3.SORT_ASCENDING)

    assert (result == expected_result)

def test_zero_numbers_entered():
    result = []
    input_arr = []
    expected_result = 0

    result =Lab3.bubble_sort(input_arr, Lab3.SORT_ASCENDING)

    assert (result == expected_result)

def test_not_integer_values():
    result = []
    input_arr = [12.1, 23, 45, 54, 67, 1, 3, 5]
    expected_result = 2

    result =Lab3.bubble_sort(input_arr, Lab3.SORT_ASCENDING)

    assert (result == expected_result)