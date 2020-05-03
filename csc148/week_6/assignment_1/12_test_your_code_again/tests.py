# TODO: put all your tests in this file (you can delete this line)

import pytest
import unittest
from typing import List
from course import Course, Student
from grouper import AlphaGrouper, GreedyGrouper, RandomGrouper, WindowGrouper
from survey import (Answer, CheckboxQuestion, MultipleChoiceQuestion,
                    NumericQuestion, Question, Survey, YesNoQuestion,
                    InvalidAnswerError)

@pytest.fixture
def student():
    """Initializes a student with name Simon"""
    return Student(1, 'Simon')

@pytest.fixture
def course():
    """Initializes a course with name CSC148"""
    return Course('CSC148')

@pytest.fixture
def multiple_choice_question() -> MultipleChoiceQuestion:
    return MultipleChoiceQuestion(1, "Multiplechoice Question", ["A","B","C","D"])

@pytest.fixture
def numeric_question() -> NumericQuestion:
    return NumericQuestion(1, "Numeric Question", 1, 10)

@pytest.fixture
def yes_no_question() -> YesNoQuestion:
    return YesNoQuestion(1, "YesNo Question")

@pytest.fixture
def checkbox_question() -> CheckboxQuestion:
    return CheckboxQuestion(1, "Checkbox Question", ["A","B","C"])

"""
Student Class
"""

class TestStudent:
    def test_str_method_should_return_simon_as_student_name(self, student, multiple_choice_question):
        expected = 'Simon'
        result = student.name
        assert expected == result

    def test_set_answer_method_should_return_1_for_the_length_of_answers_keys(self, student, multiple_choice_question):
        q = multiple_choice_question
        a = Answer('A')
        student.set_answer(q, a)

        expected = 1

        result = len(list(dict.keys(student.answers)))

        assert expected == result

    def test_set_method_should_return_1_for_the_key_in_answers(self, student, multiple_choice_question):
        q = multiple_choice_question
        a = Answer('A')
        student.set_answer(q, a)

        expected = 1

        result = list(dict.keys(student.answers))[0]

        assert expected == result

    def test_set_method_should_return_False_when_student_does_not_have_answer_to_question(self, student, multiple_choice_question):
        q1 = multiple_choice_question
        q2 = MultipleChoiceQuestion(3, 'Question', ["A","B","C","D"])
        a1 = Answer('A')

        student.set_answer(q1, a1)
        expected = False

        result = student.has_answer(q2)

        assert result == expected

    def test_get_answer_method_should_return_Answer_with_content_A(self, student, multiple_choice_question):
        q1 = multiple_choice_question
        a1 = Answer('A')

        student.set_answer(q1, a1)
        expected = 'A'

        result = student.get_answer(q1).content

        assert result == expected


"""
Course Class
"""

class TestCourse:
    def test_enroll_students_method_should_cause_students_attribute_should_have_length_of_1(self, course, student):
        course.enroll_students([student])
        expected = 1

        result = len(course.students)

        assert expected == result

    def test_enroll_students_method_should_cause_student_in_students_attribute_to_have_name_simon(self, course, student):
        course.enroll_students([student])
        expected = 'Simon'

        result = course.students[0].name

        assert expected == result

    def test_enroll_students_method_should_cause_students_attribute_to_have_length_of_1(self, course, student):

        course.enroll_students([student])
        expected = 1

        course.enroll_students([student])
        result = len(course.students)

        assert expected == result

    def test_all_answered_method_should_return_True_when_survey_questions_dont_exist(self, course):
        survey = Survey([])
        expected = True

        result = course.all_answered(survey)

        assert expected == result

    def test_get_students_method_should_return_all_added_students_in_increasing_order_by_id(self, course):
        s1 = Student(1, 'John')
        s2 = Student(2, 'Mary')
        survey = course.enroll_students([s2,s1])
        expected = [s1,s2]

        result = course.get_students()

        assert expected == result



if __name__ == '__main__':
    pytest.main(['tests.py'])
