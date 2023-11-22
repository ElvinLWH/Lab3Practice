import employee_info

dictionary = employee_info.employee_data
def test_get_employees_by_age_range():

    expected_result = [dictionary[5]]

    result = employee_info.get_employees_by_age_range(39, 41)

    assert (result == expected_result)

def test_calculate_average_salary():

    expected_result = 361000/6

    result = employee_info.calculate_average_salary()

    assert (result == expected_result)

def test_get_employees_by_dept():

    expected_result = [dictionary[3], dictionary[4]]

    result = employee_info.get_employees_by_dept("Engineering")

    assert (result == expected_result)

