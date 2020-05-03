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

"""
Test for student.__str__
"""
class TestStudent:
    def test_str_method_should_return_simon_as_student_name(self, student):
        expected = 'Simon'
        result = student.name
        assert expected == result

    def test_set_answer_method_should_return_1_for_the_length_of_answers_keys(self, student):
        q = Question(2, 'Question')
        a = Answer('Answer')
        student.set_answer(q, a)

        expected = 1

        result = len(list(dict.keys(student.answers)))

        assert expected == result

    def test_set_method_should_return_2_for_the_key_in_answers(self, student):
        q = Question(2, 'Question')
        a = Answer('Answer')
        student.set_answer(q, a)

        expected = 2

        result = list(dict.keys(student.answers))[0]

        assert expected == result

    def test_set_method_should_return_False_when_student_does_not_have_answer_to_question(self, student):
        q1 = Question(2, 'Question')
        q2 = Question(3, 'Question')
        a1 = Answer('Answer')

        student.set_answer(q1, a1)
        expected = False

        result = student.has_answer(q2)

        assert result == expected

    def test_get_answer_method_should_return_Answer_with_content_answer(self, student):
        q1 = Question(2, 'Question')
        a1 = Answer('answer')

        student.set_answer(q1, a1)
        expected = 'answer'

        result = student.get_answer(q1).content

        assert result == expected


