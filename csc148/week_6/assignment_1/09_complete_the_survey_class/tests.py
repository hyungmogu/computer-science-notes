# TODO: put all your tests in this file (you can delete this line)

import pytest
import unittest

from course import Student
from grouper import Group, Grouping
from survey import (Answer, CheckboxQuestion, MultipleChoiceQuestion,
                    NumericQuestion, Survey, YesNoQuestion)
from criterion import (HomogeneousCriterion, HeterogeneousCriterion,
                       LonelyMemberCriterion, InvalidAnswerError)

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

    def test_contains_method_should_return_False_if_question_does_not_exists(self, survey):
        question = MultipleChoiceQuestion(5, "Multiplechoice Question 2",
                                          ["A","B","C","D","E"])
        expected = False

        result = question in survey

        assert expected == result

    def test_str_method_should_return_all_questions_in_string_format(self, survey):
        expected = "1. Multiplechoice Question : A,B,C,D\n2. Numeric Question : 1 - 10\n3. YesNo Question\n4. Checkbox Question : A,B,C"

        result = str(survey)

        assert expected == result

    def test_get_questions_method_should_return_correct_length_of_questions(self, survey):
        expected = 4

        result = len(survey.get_questions())

        assert expected == result

    def test_get_questions_method_should_return_correct_questions(self):
        questions = [
            MultipleChoiceQuestion(1, "Multiplechoice Question", ["A","B","C","D"]),
            NumericQuestion(2, "Numeric Question", 1, 10),
            YesNoQuestion(3, "YesNo Question"),
            CheckboxQuestion(4, "Checkbox Question", ["A","B","C"])]
        survey = Survey(questions)

        expected = [id(question) for question in questions]

        result = [id(question) for question in survey.get_questions()]

        assert expected == result

    def test__get_criterion_method_should_return_homogeneous_criterion_if_question_doesnt_exist_in__critera(self, survey):
        question = MultipleChoiceQuestion(1, "Multiplechoice Question", ["A","B","C","D"])

        expected = True

        result = isinstance(survey._get_criterion(question), HomogeneousCriterion)

        assert expected == result

    def test__get_criterion_method_should_return_correct_criterion_if_question_exists_in__critera(self, survey):
        question = MultipleChoiceQuestion(1, "Multiplechoice Question", ["A","B","C","D"])
        survey._criteria[question.id] = LonelyMemberCriterion()

        expected = True

        result = isinstance(survey._get_criterion(question), LonelyMemberCriterion)

        assert expected == result


    def test__get_weight_method_should_return_1_if_question_doesnt_exist_in__weights(self, survey):
        question = MultipleChoiceQuestion(1, "Multiplechoice Question", ["A","B","C","D"])

        expected = 1

        result = survey._get_weight(question)

        assert expected == result

    def test__get_weight_method_should_return_correct_weight_if_question_exists_in__weights(self, survey):
        question = MultipleChoiceQuestion(1, "Multiplechoice Question", ["A","B","C","D"])
        survey._weights[question.id] = 10

        expected = 10

        result = survey._get_weight(question)

        assert expected == result

    def test_set_weight_method_should_return_False_if_question_doesnt_exist_in__questions(self, survey):
        question = MultipleChoiceQuestion(5, "Multiplechoice Question 2", ["A","B","C","D","E"])

        expected = False

        result = survey.set_weight(10, question)

        assert expected == result

    def test_set_weight_method_should_return_True_if_question_exists_in__questions(self, survey):
        question = MultipleChoiceQuestion(1, "Multiplechoice Question", ["A","B","C","D"])

        expected = True

        result = survey.set_weight(10, question)

        assert expected == result

    def test_set_weight_method_should_store_correct_weight_if_successful(self, survey):
        question = MultipleChoiceQuestion(1, "Multiplechoice Question", ["A","B","C","D"])
        survey.set_weight(10, question)

        expected = 10

        result = survey._weights[question.id]

        assert expected == result

    def test_set_criterion_method_should_return_False_if_question_doesnt_exist_in__questions(self, survey):
        question = MultipleChoiceQuestion(5, "Multiplechoice Question 2", ["A","B","C","D","E"])

        expected = False

        result = survey.set_criterion(HomogeneousCriterion(), question)

        assert expected == result

    def test_set_criterion_method_should_return_True_if_question_exists_in__questions(self, survey):
        question = MultipleChoiceQuestion(1, "Multiplechoice Question", ["A","B","C","D"])

        expected = True

        result = survey.set_criterion(HomogeneousCriterion(), question)

        assert expected == result

    def test_set_criterion_method_should_store_correct_criterion_if_successful(self, survey):
        question = MultipleChoiceQuestion(1, "Multiplechoice Question", ["A","B","C","D"])
        survey.set_criterion(HomogeneousCriterion(), question)

        expected = True

        result = isinstance(survey._criteria[question.id], HomogeneousCriterion)

        assert expected == result


