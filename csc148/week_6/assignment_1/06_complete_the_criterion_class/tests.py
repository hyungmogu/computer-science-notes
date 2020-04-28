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


class TestHeterogeneousCriterion:
    pass

class TestLonelyMemberCriterion:
    pass