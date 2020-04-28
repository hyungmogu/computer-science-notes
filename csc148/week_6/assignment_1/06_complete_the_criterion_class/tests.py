# TODO: put all your tests in this file (you can delete this line)

import pytest
import unittest
from course import Student, Course
from survey import (Question, MultipleChoiceQuestion, NumericQuestion,
                    YesNoQuestion, CheckboxQuestion, Answer)

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

class TestAnswer:
    def test_is_valid_method_should_return_True_for_all_valid_answers_to_mc_question(self,multiple_choice_question):
        expected = True
        for val in ["A","B","C","D"]:
            answer = Answer(val)
            result = answer.is_valid(multiple_choice_question)
            assert expected == result

    def test_is_valid_method_should_return_False_for_invalid_answers_to_mc_question(self,multiple_choice_question):
        answer1 = Answer("E")
        answer2 = Answer(1)
        answer3 = Answer(True)
        answer4 = Answer(["A","B"])

        expected = False

        result1 = answer1.is_valid(multiple_choice_question)
        result2 = answer2.is_valid(multiple_choice_question)
        result3 = answer3.is_valid(multiple_choice_question)
        result4 = answer4.is_valid(multiple_choice_question)

        assert expected == result1
        assert expected == result2
        assert expected == result3
        assert expected == result4

    def test_is_valid_method_should_return_True_for_all_valid_answers_to_numeric_question(self,numeric_question):
        expected = True

        for value in range(1,11):
            answer = Answer(value)
            result = answer.is_valid(numeric_question)
            assert expected == result

    def test_is_valid_method_should_return_False_for_invalid_answers_to_numeric_question(self,numeric_question):
        answer1 = Answer(0)
        answer2 = Answer(11)
        answer3 = Answer(True)
        answer4 = Answer("A")
        answer5 = Answer(["A","B"])

        expected = False

        result1 = answer1.is_valid(numeric_question)
        result2 = answer2.is_valid(numeric_question)
        result3 = answer3.is_valid(numeric_question)
        result4 = answer4.is_valid(numeric_question)
        result5 = answer5.is_valid(numeric_question)

        assert expected == result1
        assert expected == result2
        assert expected == result3
        assert expected == result4
        assert expected == result5

    def test_is_valid_method_should_return_True_for_all_valid_answers_to_yesno_question(self,yes_no_question):
        expected = True

        for value in [True, False]:
            answer = Answer(value)
            result = answer.is_valid(yes_no_question)
            assert expected == result

    def test_is_valid_method_should_return_False_for_invalid_answers_to_yesno_question(self,yes_no_question):
        answer1 = Answer(0)
        answer2 = Answer(1)
        answer3 = Answer(11)
        answer4 = Answer("A")
        answer5 = Answer(["A","B"])

        expected = False

        result1 = answer1.is_valid(yes_no_question)
        result2 = answer2.is_valid(yes_no_question)
        result3 = answer3.is_valid(yes_no_question)
        result4 = answer4.is_valid(yes_no_question)
        result5 = answer5.is_valid(yes_no_question)

        assert expected == result1
        assert expected == result2
        assert expected == result3
        assert expected == result4
        assert expected == result5

    def test_is_valid_method_should_return_True_for_all_valid_answers_to_checkbox_question(self,checkbox_question):
        answer = Answer(["A","B","C"])

        expected = True

        result = answer.is_valid(checkbox_question)
        assert expected == result

    def test_is_valid_method_should_return_False_for_invalid_answers_to_checkbox_question(self,checkbox_question):
        answer1 = Answer(11)
        answer2 = Answer(True)
        answer3 = Answer(False)
        answer4 = Answer("A")
        answer5 = Answer(["E","F","G"])

        expected = False

        result1 = answer1.is_valid(checkbox_question)
        result2 = answer2.is_valid(checkbox_question)
        result3 = answer3.is_valid(checkbox_question)
        result4 = answer4.is_valid(checkbox_question)
        result5 = answer5.is_valid(checkbox_question)

        assert expected == result1
        assert expected == result2
        assert expected == result3
        assert expected == result4
        assert expected == result5