import pytest
from employee_info import get_employees_by_age_range, calculate_average_salary, get_employees_by_dept

def test_get_employees_by_age_range():
    result = get_employees_by_age_range(24, 36)
    assert all(24 < emp["age"] < 36 for emp in result)

def test_calculate_average_salary():
    avg = calculate_average_salary()
    expected_avg = (50000 + 60000 + 56000 + 70000 + 65000 + 60000) / 6
    assert avg == expected_avg

def test_get_employees_by_dept():
    marketing_employees = get_employees_by_dept("Marketing")
    assert all(emp["department"] == "Marketing" for emp in marketing_employees)
