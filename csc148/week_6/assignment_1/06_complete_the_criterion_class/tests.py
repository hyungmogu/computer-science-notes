# TODO: put all your tests in this file (you can delete this line)

import pytest
import unittest
from criterion import (HomogeneousCriterion, HeterogeneousCriterion,
                       LonelyMemberCriterion, InvalidAnswerError)
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


@pytest.fixture
def homogeneous_criterion() -> HomogeneousCriterion:
    return HomogeneousCriterion()

@pytest.fixture
def hetrogeneous_criterion() -> HeterogeneousCriterion:
    return HeterogeneousCriterion()

@pytest.fixture
def lonely_member_criterion() -> LonelyMemberCriterion:
    return LonelyMemberCriterion()


class TestHomogeneousCriterion:
    def test_score_answers_should_raise_invalidAnswer_for_mc_question_if_an_answer_is_not_valid(self,homogeneous_criterion, multiple_choice_question):
        answers = [Answer("E"), Answer("D")]

        with pytest.raises(InvalidAnswerError):
            homogeneous_criterion.score_answers(multiple_choice_question, answers)

    def test_score_answers_should_raise_invalidAnswer_for_numeric_question_if_an_answer_is_not_valid(self,homogeneous_criterion, numeric_question):
        answers = [Answer(1), Answer(0), Answer("E")]

        with pytest.raises(InvalidAnswerError):
            homogeneous_criterion.score_answers(numeric_question, answers)

    def test_score_answers_should_raise_invalidAnswer_for_yesno_question_if_an_answer_is_not_valid(self,homogeneous_criterion, yes_no_question):
        answers = [Answer(True), Answer(False), Answer("E")]

        with pytest.raises(InvalidAnswerError):
            homogeneous_criterion.score_answers(yes_no_question, answers)

    def test_score_answers_should_raise_invalidAnswer_for_checkbox_question_if_an_answer_is_not_valid(self,homogeneous_criterion, checkbox_question):
        answers = [Answer(True), Answer("B"), Answer("C")]

        with pytest.raises(InvalidAnswerError):
            homogeneous_criterion.score_answers(checkbox_question, answers)

    def test_score_answers_should_return_1_if_single_valid_answer_exists_for_mc_question(self, homogeneous_criterion, multiple_choice_question):
        answers = [Answer("A")]
        expected = 1.0

        result = homogeneous_criterion.score_answers(multiple_choice_question, answers)

        assert expected == result

    def test_score_answers_should_return_1_if_single_valid_answer_exists_for_numeric_question(self, homogeneous_criterion, numeric_question):
        answers = [Answer(1)]
        expected = 1.0

        result = homogeneous_criterion.score_answers(numeric_question, answers)

        assert expected == result

    def test_score_answers_should_return_1_if_single_valid_answer_exists_for_yesno_question(self, homogeneous_criterion, yes_no_question):
        answers = [Answer(True)]
        expected = 1.0

        result = homogeneous_criterion.score_answers(yes_no_question, answers)

        assert expected == result

    def test_score_answers_should_return_1_if_single_valid_answer_exists_for_checkbox(self, homogeneous_criterion, checkbox_question):
        answers = [Answer(["A", "B"])]
        expected = 1.0

        result = homogeneous_criterion.score_answers(checkbox_question, answers)

        assert expected == result

    def test_score_answers_should_return_correct_value_if_all_is_well_for_mc_question(self, homogeneous_criterion, multiple_choice_question):
        answers1 = [Answer("B"), Answer("B"), Answer("B")]
        answers2 = [Answer("A"), Answer("B"), Answer("C")]
        expected1 = 1.0
        expected2 = 0.0

        result1 = homogeneous_criterion.score_answers(multiple_choice_question, answers1)
        result2 = homogeneous_criterion.score_answers(multiple_choice_question, answers2)

        assert expected1 == result1
        assert expected2 == result2

    def test_score_answers_should_return_correct_value_if_all_is_well_for_numeric_question(self, homogeneous_criterion, numeric_question):
        answers1 = [Answer(1), Answer(1), Answer(1)]
        answers2 = [Answer(1), Answer(10)]
        expected1 = 1.0
        expected2 = 0.0

        result1 = homogeneous_criterion.score_answers(numeric_question, answers1)
        result2 = homogeneous_criterion.score_answers(numeric_question, answers2)

        assert expected1 == result1
        assert expected2 == result2

    def test_score_answers_should_return_correct_value_if_all_is_well_for_yesno_question(self, homogeneous_criterion, yes_no_question):
        answers1 = [Answer(True), Answer(True), Answer(True)]
        answers2 = [Answer(False), Answer(True)]
        expected1 = 1.0
        expected2 = 0.0

        result1 = homogeneous_criterion.score_answers(yes_no_question, answers1)
        result2 = homogeneous_criterion.score_answers(yes_no_question, answers2)

        assert expected1 == result1
        assert expected2 == result2


    def test_score_answers_should_return_correct_value_if_all_is_well_for_checkbox_question(self, homogeneous_criterion, checkbox_question):
        answers1 = [Answer(["A","B","C"]), Answer(["A","B","C"]), Answer(["A","B","C"])]
        answers2 = [Answer(["A"]), Answer(["B"]), Answer(["C"])]
        expected1 = 1.0
        expected2 = 0.0

        result1 = homogeneous_criterion.score_answers(checkbox_question, answers1)
        result2 = homogeneous_criterion.score_answers(checkbox_question, answers2)

        assert expected1 == result1
        assert expected2 == result2


class TestHeterogeneousCriterion:
    pass

class TestLonelyMemberCriterion:
    pass