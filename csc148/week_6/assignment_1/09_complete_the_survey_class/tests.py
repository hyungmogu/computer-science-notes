# TODO: put all your tests in this file (you can delete this line)

import pytest
import unittest
from typing import List

from course import Student
from grouper import Group, Grouping
from survey import (Answer, CheckboxQuestion, MultipleChoiceQuestion,
                    NumericQuestion, Question, Survey, YesNoQuestion,
                    InvalidAnswerError)
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

@pytest.fixture
def students() -> List[Student]:
    return [Student(1, "John"), Student(2, "Mary"), Student(3, "Simon")]

@pytest.fixture
def students_2() -> List[Student]:
    return [Student(4, "Nanny"), Student(5, "Dilbert"), Student(6, "Jason")]

@pytest.fixture
def mc_questions() -> List[Question]:
    return [MultipleChoiceQuestion(1, "Multiplechoice Question", ["A","B","C","D"]),
            MultipleChoiceQuestion(2, "Multiplechoice Question", ["A","B","C","D"]),
            MultipleChoiceQuestion(3, "Multiplechoice Question", ["A","B","C","D"]),
            MultipleChoiceQuestion(4, "Multiplechoice Question", ["A","B","C","D"])]

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

    def test_score_students_method_should_return_0_if_quesetions_dont_exist(self, students):
        survey = Survey([])
        students = [Student(1, "John"), Student(2, "Mary"), Student(3, "Simon")]

        expected = 0

        result = survey.score_students(students)

        assert expected == result

    def test_score_students_method_should_return_0_if_more_than_1_question_exists_but_answer_is_invalid(self, survey, students):
        questions = survey.get_questions()
        students = [Student(1, "John"), Student(2, "Mary"), Student(3, "Simon")]

        for student in students:
            for question in questions:
                if question.id == 1:
                    answer = Answer("E")
                elif question.id == 2:
                    answer = Answer(2)
                elif question.id == 3:
                    answer = Answer(True)
                else:
                    answer = Answer(["A","B"])

                student.set_answer(question, answer)

        expected = 0

        result = survey.score_students(students)

        assert expected == result

    def test_score_students_method_should_return_correct_value_if_all_is_well_for_homogeneous_criterion(self, students, students_2, mc_questions):
        survey = Survey(mc_questions)

        for student in students:
            for question in mc_questions:
                answer = Answer("A")
                student.set_answer(question, answer)

        for student in students_2:
            for question in mc_questions:
                if question.id == 1:
                    answer = Answer("A")
                elif question.id == 2:
                    answer = Answer("B")
                elif question.id == 3:
                    answer = Answer("C")
                elif question.id == 4:
                    answer = Answer("D")
                student.set_answer(question, answer)

        expected_1 = 1.0
        expected_2 = 0.0

        result_1 = survey.score_students(students)
        result_2 = survey.score_students(students_2)

        assert expected_1 == result_1
        assert expected_2 == result_2

    def test_score_students_method_should_return_correct_value_if_all_is_well_for_hetrogeneous_criterion(self, students, students_2, mc_questions):
        survey = Survey(mc_questions)

        for student in students:
            for question in mc_questions:
                answer = Answer("A")
                survey.set_criterion(HeterogeneousCriterion(), question)
                student.set_answer(question, answer)

        for student in students_2:
            for question in mc_questions:
                if question.id == 1:
                    answer = Answer("A")
                elif question.id == 2:
                    answer = Answer("B")
                elif question.id == 3:
                    answer = Answer("C")
                elif question.id == 4:
                    answer = Answer("D")
                survey.set_criterion(HeterogeneousCriterion(), question)
                student.set_answer(question, answer)

        expected_1 = 0.0
        expected_2 = 1.0

        result_1 = survey.score_students(students)
        result_2 = survey.score_students(students_2)

        assert expected_1 == result_1
        assert expected_2 == result_2

    def test_score_students_method_should_return_correct_value_if_all_is_well_for_lonely_member_criterion(self, students, students_2, mc_questions):
        survey = Survey(mc_questions)

        for student in students:
            for question in mc_questions:
                answer = Answer("A")
                survey.set_criterion(LonelyMemberCriterion(), question)
                student.set_answer(question, answer)

        for student in students_2:
            for question in mc_questions:
                if question.id == 1:
                    answer = Answer("A")
                else:
                    answer = Answer("B")

                survey.set_criterion(LonelyMemberCriterion(), question)
                student.set_answer(question, answer)

        expected_1 = 1.0
        expected_2 = 0.0

        result_1 = survey.score_students(students)
        result_2 = survey.score_students(students_2)

        assert expected_1 == result_1
        assert expected_2 == result_2