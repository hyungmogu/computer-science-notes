# TODO: put all your tests in this file (you can delete this line)

import pytest
import unittest

from course import Student
from grouper import Group, Grouping
from survey import (Answer, CheckboxQuestion, MultipleChoiceQuestion,
                    NumericQuestion, Survey, YesNoQuestion)


@pytest.fixture
def grouping() -> Grouping:
    group1 = Group([Student(1, "John"), Student(2, "Mary"), Student(3, "Simon")])
    group2 = Group([Student(4, "Nanny"), Student(5, "Dilbert"), Student(6, "Jason")])

    grouping = Grouping()
    grouping._groups = [group1, group2]
    return grouping

@pytest.fixture
def survey() -> Survey:
    questions = [
        MultipleChoiceQuestion(1, "Multiplechoice Question", ["A","B","C","D"]),
        NumericQuestion(2, "Numeric Question", 1, 10),
        YesNoQuestion(3, "YesNo Question"),
        CheckboxQuestion(4, "Checkbox Question", ["A","B","C"])]

    survey = Survey(questions)
    return survey

class TestSurvey:

    def test_len_method_should_return_correct_length_of_questions(self, survey):
        expected = 4

        result = len(survey)

        assert expected == result


    def test_contains_method_should_return_True_if_question_exists(self, survey):
        question = MultipleChoiceQuestion(1, "Multiplechoice Question",
                                          ["A","B","C","D"])
        expected = True

        result = question in survey

        assert expected == result