# TODO: put all your tests in this file (you can delete this line)

import pytest
import unittest
from typing import List
from course import Course, Student
from grouper import AlphaGrouper, GreedyGrouper, RandomGrouper
from survey import (Answer, CheckboxQuestion, MultipleChoiceQuestion,
                    NumericQuestion, Question, Survey, YesNoQuestion,
                    InvalidAnswerError)

#========= code from task 2 =========
@pytest.fixture
def course():
    """Initializes a course with name CSC148"""
    return Course('CSC148')
# ===================================

#========= code from task 9 =========

@pytest.fixture
def survey() -> Survey:
    questions = [
        MultipleChoiceQuestion(1, "Multiplechoice Question", ["A","B","C","D"]),
        NumericQuestion(2, "Numeric Question", 1, 10),
        YesNoQuestion(3, "YesNo Question"),
        CheckboxQuestion(4, "Checkbox Question", ["A","B","C"])]

    survey = Survey(questions)
    return survey
# ===================================

@pytest.fixture
def students_lst() -> List[Student]:
    return [Student(1, "Jason"), Student(2, "Mary"), Student(3, "Simon"), Student(4, "Jessie")]

class TestAlphaGrouper:
    def test_make_grouping_method_should_return_correct_value(self, course, survey, students_lst):
        course.enroll_students(students_lst)

        expected = "Jason,Jessie\nMary,Simon"

        grouper = AlphaGrouper(2)
        result = str(grouper.make_grouping(course, survey))

        assert expected == result


class TestRandomGrouper:
    def test_make_grouping_method_should_return_grouping_of_randomly_grouped_students(self, course, survey, students_lst):
        course.enroll_students(students_lst)

        expected = True

        grouper1 = RandomGrouper(2)
        grouper2 = RandomGrouper(2)

        result = str(grouper1.make_grouping(course, survey)) != str(grouper2.make_grouping(course, survey))

        assert expected == result


class TestGreedyGrouper:
    def test_make_grouping_method_should_return_grouping_with_each_group_in_decreasing_student_score(self, course, survey, students_lst):

        for question in survey.get_questions():
            if question.id == 1:
                students_lst[0].set_answer(question, Answer("A"))
                students_lst[1].set_answer(question, Answer("B"))
                students_lst[2].set_answer(question, Answer("A"))
                students_lst[3].set_answer(question, Answer("B"))
            elif question.id == 2:
                students_lst[0].set_answer(question, Answer(1))
                students_lst[1].set_answer(question, Answer(2))
                students_lst[2].set_answer(question, Answer(1))
                students_lst[3].set_answer(question, Answer(2))
            elif question.id == 3:
                students_lst[0].set_answer(question, Answer(True))
                students_lst[1].set_answer(question, Answer(False))
                students_lst[2].set_answer(question, Answer(True))
                students_lst[3].set_answer(question, Answer(False))
            elif question.id == 4:
                students_lst[0].set_answer(question, Answer(["A","B"]))
                students_lst[1].set_answer(question, Answer(["A","B"]))
                students_lst[2].set_answer(question, Answer(["A","B"]))
                students_lst[3].set_answer(question, Answer(["A","B"]))

        course.enroll_students(students_lst)
        expected = ''
        result = str(GreedyGrouper(2).make_grouping(course, survey))

        assert expected == result