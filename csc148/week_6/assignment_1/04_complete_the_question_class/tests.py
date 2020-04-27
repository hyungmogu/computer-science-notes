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

class TestMultipleChoiceQuestion:
    def test_the_class_should_be_inheritance_of_Question_class(self, multiple_choice_question):
        expected = True

        result = issubclass(MultipleChoiceQuestion, Question)

        assert expected == result

    def test_the_class_should_return_correct_string_on_typcasting_to_str(self, multiple_choice_question):
        expected = "1. Multiplechoice Question : A,B,C,D"

        result = str(multiple_choice_question)

        assert expected == result

    def test_validate_answer_method_should_return_True_if_the_answer_is_valid(self,multiple_choice_question):
        answer = Answer("B")

        expected = True

        result = multiple_choice_question.validate_answer(answer)

        assert expected == result

    def test_validate_answer_method_should_return_False_if_the_answer_is_not_valid(self, multiple_choice_question):
        answer = Answer("E")

        expected = False

        result = multiple_choice_question.validate_answer(answer)

        assert expected == result

    def test_get_similarity_method_should_return_1_if_two_answers_are_equal(self, multiple_choice_question):
        answer1 = Answer("B")
        answer2 = Answer("B")

        expected = 1.0

        result = multiple_choice_question.get_similarity(answer1, answer2)

        assert expected == result

    def test_get_similarity_method_should_return_0_if_two_answers_are_not_equal(self, multiple_choice_question):
        answer1 = Answer("B")
        answer2 = Answer("D")

        expected = 0.0

        result = multiple_choice_question.get_similarity(answer1, answer2)

        assert expected == result


class TestNumericQuestion:
    def test_the_class_should_be_inheritance_of_Question_class(self, numeric_question):
        expected = True

        result = issubclass(NumericQuestion, Question)

        assert expected == result

    def test_the_class_should_return_correct_string_on_typcasting_to_str(self, numeric_question):
        expected = "1. Numeric Question : 1 - 10"

        result = str(numeric_question)

        assert expected == result

    def test_validate_answer_method_should_return_True_if_the_answer_is_valid(self,numeric_question):
        answer = Answer(1)

        expected = True

        result = numeric_question.validate_answer(answer)

        assert expected == result

    def test_validate_answer_method_should_return_False_if_answer_is_not_integer(self, numeric_question):
        answer = Answer("E")

        expected = False

        result = numeric_question.validate_answer(answer)

        assert expected == result

    def test_validate_answer_method_should_return_False_if_answer_is_out_of_bound(self, numeric_question):
        answer1 = Answer(0)
        answer2 = Answer(11)

        expected = False

        result1 = numeric_question.validate_answer(answer1)
        result2 = numeric_question.validate_answer(answer2)

        assert expected == result1
        assert expected == result2

    def test_get_similarity_method_should_return_1_if_answer1_eq_answer2(self, numeric_question):
        answer1 = Answer(5)
        answer2 = Answer(5)

        expected = 1.0

        result = numeric_question.get_similarity(answer1, answer2)

        assert expected == result

    def test_get_similarity_method_should_return_0_if_answer1_is_min_and_answer2_is_max(self, numeric_question):
        answer1 = Answer(1)
        answer2 = Answer(10)

        expected = 0.0

        result = numeric_question.get_similarity(answer1, answer2)

        assert expected == result


class TestYesNoQuestion:
    def test_the_class_should_be_inheritance_of_Question_class(self, yes_no_question):
        expected = True

        result = issubclass(YesNoQuestion, Question)

        assert expected == result

    def test_the_class_should_return_correct_string_on_typcasting_to_str(self, yes_no_question):
        expected = "1. YesNo Question"

        result = str(yes_no_question)

        assert expected == result

    def test_validate_answer_method_should_return_True_if_the_answer_is_boolean(self,yes_no_question):
        answer1 = Answer(True)
        answer2 = Answer(False)

        expected = True

        result1 = yes_no_question.validate_answer(answer1)
        result2 = yes_no_question.validate_answer(answer2)

        assert expected == result1
        assert expected == result2

    def test_validate_answer_method_should_return_False_if_answer_is_not_boolean(self, yes_no_question):
        answer1 = Answer("E")
        answer2 = Answer(1)
        answer3 = Answer(['a','b','c'])

        expected = False

        result1 = yes_no_question.validate_answer(answer1)
        result2 = yes_no_question.validate_answer(answer2)
        result3 = yes_no_question.validate_answer(answer3)

        assert expected == result1
        assert expected == result2
        assert expected == result3

    def test_get_similarity_method_should_return_1_if_two_answers_are_equal(self, yes_no_question):
        answer1 = Answer(True)
        answer2 = Answer(True)

        expected = 1.0

        result = yes_no_question.get_similarity(answer1, answer2)

        assert expected == result

    def test_get_similarity_method_should_return_0_if_two_answers_are_not_equal(self, yes_no_question):
        answer1 = Answer(True)
        answer2 = Answer(False)

        expected = 0.0

        result = yes_no_question.get_similarity(answer1, answer2)

        assert expected == result


class CheckboxQuestion:

    def test_the_class_should_be_inheritance_of_MultipleChoiceQuestion_class(self, checkbox_question):
        expected = True

        result = issubclass(CheckboxQuestion, MultipleChoiceQuestion)

        assert expected == result

    def test_the_class_should_return_correct_string_on_typcasting_to_str(self, checkbox_question):
        expected = "1. Checkbox Question : A,B,C"

        result = str(checkbox_question)

        assert expected == result

