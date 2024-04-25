import pytest
from student import Student
from search import *
@pytest.mark.parametrize("students", [
    [],
    [Student(id) for id in range(1,100)],
    [Student(id) for id in [1,2,3,5,6,8,10,22,23,33,45,88]]
])
@pytest.mark.parametrize("target_id", [
    id for id in range(0,100)
])
def test_student_with_id(students,target_id):
    lineair_result = lineair_search(students,target_id)
    binary_result = binary_search(students,target_id)
    assert lineair_result is binary_result, f"failed when looking for id = {target_id}"