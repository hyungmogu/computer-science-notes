# TODO: put all your tests in this file (you can delete this line)

import pytest
from course import Student, Course
from survey import Question, Answer, Survey

@pytest.fixture
def course():
    """Initializes a course with name CSC148"""
    return Course('CSC148')

"""
Test for course.enroll_students()
"""

def test_students_attribute_should_have_length_of_1(course):
    student = Student(1, 'John')
    course.enroll_students([student])
    expected = 1

    result = len(course.students)

    assert expected == result

def test_the_enrolled_student_in_students_attribute_should_have_name_john(course):
    student = Student(1, 'John')
    course.enroll_students([student])
    expected = 'John'

    result = course.students[0].name

    assert expected == result

def test_students_attribute_should_have_length_of_1_after_enrolling_the_same_student(course):
    student = Student(1, 'John')

    course.enroll_students([student])
    expected = 1

    course.enroll_students([student])
    result = len(course.students)

    assert expected == result

"""
Test for course.all_answered()
"""

# TODO: NEEDS TO COMEBACK LATER
def test_all_answered_method_should_return_False_when_survey_questions_dont_exist(course):
    survey = Survey([])
    expected = False

    result = course.all_answered(survey)

    assert expected == result


"""
Test for course.get_students()
"""

def test_get_students_method_should_return_all_added_students_in_increasing_order_by_id(course):
    s1 = Student(1, 'John')
    s2 = Student(2, 'Mary')
    survey = course.enroll_students([s2,s1])
    expected = [s1,s2]

    result = course.get_students()

    assert expected == result

