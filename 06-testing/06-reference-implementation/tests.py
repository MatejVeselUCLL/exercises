import pytest
from search import binary_search, linear_search

class Student:
    def __init__(self, id):
        self.id = id

students = [
    Student(-500),
    Student(-5),
    Student(-3),
    Student(0),
    Student(1),
    Student(2),
    Student(3),
    Student(5),
    Student(100)
]
@pytest.mark.parametrize('students, target_id', [
    (students, 10000),
    (students, 77),
    (students, 0),
    (students, 2),
    (students, 1),
    (students, 5),
    ([], 5)
])
def test_binary_search(students, target_id):
    expected = binary_search(students, target_id)
    received = linear_search(students, target_id)
    assert expected == received, f"Expected {expected} Received {received}"
