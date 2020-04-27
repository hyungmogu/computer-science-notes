# TODO: put all your tests in this file (you can delete this line)

import pytest
from course import Student
from survey import Question, Answer

@pytest.fixture
def student():
    """Initializes a student with name Simon"""
    return Student(1, 'Simon')

def test_student__str__(student):
    expected = 'Simon'
    assert student.name == expected


def test_student_set_answer(student):
    q = Question(2, 'Question')
    a = Answer('Answer')
    student.set_answer(q, a)

    expected_1 = 'Question'
    expected_2 = 2
    expected_3 = 'Answer'

    keys = list(dict.keys(student.answers))

    result_1 = keys[0].text
    result_2 = keys[0].id
    result_3 = student.answers[q].content

    assert result_1 == expected_1
    assert result_2 == expected_2
    assert result_3 == expected_3
