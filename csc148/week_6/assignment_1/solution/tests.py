# TODO: put all your tests in this file (you can delete this line)

import pytest
import unittest
from typing import List
from course import Course, Student
from grouper import (AlphaGrouper, Group, Grouping, GreedyGrouper,
                     RandomGrouper, slice_list, windows, WindowGrouper)
from survey import (Answer, CheckboxQuestion, MultipleChoiceQuestion,
                    NumericQuestion, Question, Survey, YesNoQuestion,
                    InvalidAnswerError)
from criterion import (HomogeneousCriterion, HeterogeneousCriterion,
                       LonelyMemberCriterion, InvalidAnswerError)

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


@pytest.fixture
def homogeneous_criterion() -> HomogeneousCriterion:
    return HomogeneousCriterion()

@pytest.fixture
def hetrogeneous_criterion() -> HeterogeneousCriterion:
    return HeterogeneousCriterion()

@pytest.fixture
def lonely_member_criterion() -> LonelyMemberCriterion:
    return LonelyMemberCriterion()


@pytest.fixture
def group() -> Group:
    return Group([Student(1, "John"), Student(2, "Mary"), Student(3, "Simon")])

@pytest.fixture
def group_empty() -> Group:
    return Group([])


@pytest.fixture
def grouping() -> Grouping:
    group1 = Group([Student(1, "John"), Student(2, "Mary"), Student(3, "Simon")])
    group2 = Group([Student(4, "Nanny"), Student(5, "Dilbert"), Student(6, "Jason")])

    grouping = Grouping()
    grouping._groups = [group1, group2]
    return grouping


@pytest.fixture
def grouping_2() -> Grouping:
    group1 = Group([Student(7, "Johnny"), Student(8, "Marianne"), Student(9, "Sim")])
    group2 = Group([Student(10, "Nan"), Student(11, "Albert"), Student(12, "Justin")])

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


@pytest.fixture
def lst_1() -> List:
    return [3, 4, 6, 2, 3]

@pytest.fixture
def lst_2() -> List:
    return ['a', 1, 6.0, False]

@pytest.fixture
def lst_empty() -> List:
    return []


@pytest.fixture
def students_lst() -> List[Student]:
    return [Student(1, "Jason"), Student(2, "Mary"), Student(3, "Simon"), Student(4, "Jessie")]


"""
Task 2 - Student Class
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
Task 3 - Course Class
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


"""
Task 4 - Question Classes
"""


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


class TestCheckboxQuestion:
    def test_the_class_should_be_inheritance_of_MultipleChoiceQuestion_class(self, checkbox_question):
        expected = True

        result = issubclass(CheckboxQuestion, MultipleChoiceQuestion)

        assert expected == result

    def test_the_class_should_return_correct_string_on_typcasting_to_str(self, checkbox_question):
        expected = "1. Checkbox Question : A,B,C"

        result = str(checkbox_question)

        assert expected == result

    def test_validate_answer_method_should_return_false_if_not_a_list(self, checkbox_question):
        answer1 = Answer("B")
        answer2 = Answer(1)

        expected = False

        result1 = checkbox_question.validate_answer(answer1)
        result2 = checkbox_question.validate_answer(answer2)

        assert expected == result1
        assert expected == result2

    def test_validate_answer_method_should_return_false_if_empty(self, checkbox_question):
        answer = Answer([])

        expected = False

        result = checkbox_question.validate_answer(answer)

        assert expected == result

    def test_validate_answer_method_should_return_false_if_duplicate_choice_exists(self, checkbox_question):
        answer = Answer(["A","A","B"])

        expected = False

        result = checkbox_question.validate_answer(answer)

        assert expected == result

    def test_validate_answer_method_should_return_true_if_correctly_answered(self, checkbox_question):
        answer = Answer(["A","B"])

        expected = True

        result = checkbox_question.validate_answer(answer)

        assert expected == result

    def test_get_similarity_method_should_return_1_if_answer1_and_answer2_overlap_entirely(self, checkbox_question):
        answer1 = Answer(["A","B"])
        answer2 = Answer(["A","B"])

        expected = 1

        result = checkbox_question.get_similarity(answer1, answer2)

        assert expected == result

    def test_get_similarity_method_should_return_0_if_answer1_and_answer2_does_not_overlap(self, checkbox_question):
        answer1 = Answer(["A","B"])
        answer2 = Answer(["C","D"])

        expected = 0

        result = checkbox_question.get_similarity(answer1, answer2)

        assert expected == result

    def test_get_similarity_method_should_return_correct_value_if_answer1_and_answer2_overlap(self, checkbox_question):
        answer1 = Answer(["A","B"])
        answer2 = Answer(["B","D"])

        expected = 1/3

        result = checkbox_question.get_similarity(answer1, answer2)

        assert expected == result


"""
Task 5 - Answer Class
"""

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


"""
Task 6 - Criterion Classes
"""


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
    def test_score_answers_should_raise_invalidAnswer_for_mc_question_if_an_answer_is_not_valid(self,hetrogeneous_criterion, multiple_choice_question):
        answers = [Answer("E"), Answer("D")]

        with pytest.raises(InvalidAnswerError):
            hetrogeneous_criterion.score_answers(multiple_choice_question, answers)

    def test_score_answers_should_raise_invalidAnswer_for_numeric_question_if_an_answer_is_not_valid(self,hetrogeneous_criterion, numeric_question):
        answers = [Answer(1), Answer(0), Answer("E")]

        with pytest.raises(InvalidAnswerError):
            hetrogeneous_criterion.score_answers(numeric_question, answers)

    def test_score_answers_should_raise_invalidAnswer_for_yesno_question_if_an_answer_is_not_valid(self,hetrogeneous_criterion, yes_no_question):
        answers = [Answer(True), Answer(False), Answer("E")]

        with pytest.raises(InvalidAnswerError):
            hetrogeneous_criterion.score_answers(yes_no_question, answers)

    def test_score_answers_should_raise_invalidAnswer_for_checkbox_question_if_an_answer_is_not_valid(self,hetrogeneous_criterion, checkbox_question):
        answers = [Answer(True), Answer("B"), Answer("C")]

        with pytest.raises(InvalidAnswerError):
            hetrogeneous_criterion.score_answers(checkbox_question, answers)

    def test_score_answers_should_return_0_if_single_valid_answer_exists_for_mc_question(self, hetrogeneous_criterion, multiple_choice_question):
        answers = [Answer("A")]
        expected = 0.0

        result = hetrogeneous_criterion.score_answers(multiple_choice_question, answers)

        assert expected == result

    def test_score_answers_should_return_0_if_single_valid_answer_exists_for_numeric_question(self, hetrogeneous_criterion, numeric_question):
        answers = [Answer(1)]
        expected = 0.0

        result = hetrogeneous_criterion.score_answers(numeric_question, answers)

        assert expected == result

    def test_score_answers_should_return_0_if_single_valid_answer_exists_for_yesno_question(self, hetrogeneous_criterion, yes_no_question):
        answers = [Answer(True)]
        expected = 0.0

        result = hetrogeneous_criterion.score_answers(yes_no_question, answers)

        assert expected == result

    def test_score_answers_should_return_0_if_single_valid_answer_exists_for_checkbox(self, hetrogeneous_criterion, checkbox_question):
        answers = [Answer(["A", "B"])]
        expected = 0.0

        result = hetrogeneous_criterion.score_answers(checkbox_question, answers)

        assert expected == result

    def test_score_answers_should_return_correct_value_if_all_is_well_for_mc_question(self, hetrogeneous_criterion, multiple_choice_question):
        answers1 = [Answer("B"), Answer("B"), Answer("B")]
        answers2 = [Answer("A"), Answer("B"), Answer("C")]
        expected1 = 0.0
        expected2 = 1.0

        result1 = hetrogeneous_criterion.score_answers(multiple_choice_question, answers1)
        result2 = hetrogeneous_criterion.score_answers(multiple_choice_question, answers2)

        assert expected1 == result1
        assert expected2 == result2

    def test_score_answers_should_return_correct_value_if_all_is_well_for_numeric_question(self, hetrogeneous_criterion, numeric_question):
        answers1 = [Answer(1), Answer(1), Answer(1)]
        answers2 = [Answer(1), Answer(10)]
        expected1 = 0.0
        expected2 = 1.0

        result1 = hetrogeneous_criterion.score_answers(numeric_question, answers1)
        result2 = hetrogeneous_criterion.score_answers(numeric_question, answers2)

        assert expected1 == result1
        assert expected2 == result2

    def test_score_answers_should_return_correct_value_if_all_is_well_for_yesno_question(self, hetrogeneous_criterion, yes_no_question):
        answers1 = [Answer(True), Answer(True), Answer(True)]
        answers2 = [Answer(False), Answer(True)]
        expected1 = 0.0
        expected2 = 1.0

        result1 = hetrogeneous_criterion.score_answers(yes_no_question, answers1)
        result2 = hetrogeneous_criterion.score_answers(yes_no_question, answers2)

        assert expected1 == result1
        assert expected2 == result2


    def test_score_answers_should_return_correct_value_if_all_is_well_for_checkbox_question(self, hetrogeneous_criterion, checkbox_question):
        answers1 = [Answer(["A","B","C"]), Answer(["A","B","C"]), Answer(["A","B","C"])]
        answers2 = [Answer(["A"]), Answer(["B"]), Answer(["C"])]
        expected1 = 0.0
        expected2 = 1.0

        result1 = hetrogeneous_criterion.score_answers(checkbox_question, answers1)
        result2 = hetrogeneous_criterion.score_answers(checkbox_question, answers2)

        assert expected1 == result1
        assert expected2 == result2


class TestLonelyMemberCriterion:
    def test_score_answers_should_raise_invalidAnswer_for_mc_question_if_an_answer_is_not_valid(self,lonely_member_criterion, multiple_choice_question):
        answers = [Answer("A"), Answer("A"), Answer("E"), Answer("D")]

        with pytest.raises(InvalidAnswerError):
            lonely_member_criterion.score_answers(multiple_choice_question, answers)

    def test_score_answers_should_raise_invalidAnswer_for_numeric_question_if_an_answer_is_not_valid(self,lonely_member_criterion, numeric_question):
        answers = [Answer(1), Answer(0), Answer("E")]

        with pytest.raises(InvalidAnswerError):
            lonely_member_criterion.score_answers(numeric_question, answers)

    def test_score_answers_should_raise_invalidAnswer_for_yesno_question_if_an_answer_is_not_valid(self,lonely_member_criterion, yes_no_question):
        answers = [Answer(True), Answer(True), Answer("E")]

        with pytest.raises(InvalidAnswerError):
            lonely_member_criterion.score_answers(yes_no_question, answers)

    def test_score_answers_should_raise_invalidAnswer_for_checkbox_question_if_an_answer_is_not_valid(self,lonely_member_criterion, checkbox_question):
        answers = [Answer("B"), Answer("B"), Answer(True)]

        with pytest.raises(InvalidAnswerError):
            lonely_member_criterion.score_answers(checkbox_question, answers)

    def test_score_answers_should_return_correct_value_if_all_is_well_for_mc_question(self, lonely_member_criterion, multiple_choice_question):
        answers1 = [Answer("B"), Answer("B"), Answer("B")]
        answers2 = [Answer("A"), Answer("B"), Answer("A")]
        expected1 = 1.0
        expected2 = 0.0

        result1 = lonely_member_criterion.score_answers(multiple_choice_question, answers1)
        result2 = lonely_member_criterion.score_answers(multiple_choice_question, answers2)

        assert expected1 == result1
        assert expected2 == result2

    def test_score_answers_should_return_correct_value_if_all_is_well_for_numeric_question(self, lonely_member_criterion, numeric_question):
        answers1 = [Answer(1), Answer(1), Answer(1)]
        answers2 = [Answer(1), Answer(10)]
        expected1 = 1.0
        expected2 = 0.0

        result1 = lonely_member_criterion.score_answers(numeric_question, answers1)
        result2 = lonely_member_criterion.score_answers(numeric_question, answers2)

        assert expected1 == result1
        assert expected2 == result2

    def test_score_answers_should_return_correct_value_if_all_is_well_for_yesno_question(self, lonely_member_criterion, yes_no_question):
        answers1 = [Answer(True), Answer(True), Answer(True)]
        answers2 = [Answer(False), Answer(True)]
        expected1 = 1.0
        expected2 = 0.0

        result1 = lonely_member_criterion.score_answers(yes_no_question, answers1)
        result2 = lonely_member_criterion.score_answers(yes_no_question, answers2)

        assert expected1 == result1
        assert expected2 == result2


    def test_score_answers_should_return_correct_value_if_all_is_well_for_checkbox_question(self, lonely_member_criterion, checkbox_question):
        answers1 = [Answer(["A"]), Answer(["A"]), Answer(["A"])]
        answers2 = [Answer(["A"]), Answer(["B"]), Answer(["C"])]
        expected1 = 1.0
        expected2 = 0.0

        result1 = lonely_member_criterion.score_answers(checkbox_question, answers1)
        result2 = lonely_member_criterion.score_answers(checkbox_question, answers2)

        assert expected1 == result1
        assert expected2 == result2


"""
Task 7 - Group Classes
"""

class TestGroup:
    def test_len_should_return_length_of_members(self, group):
        expected = 3

        result = len(group)

        assert expected == result

    def test_contain_method_should_return_True_if_member_does_not_exist(self, group):
        member = Student(1, "John")
        expected = True

        result = member in group

        assert expected == result


    def test_contain_method_should_return_False_if_member_does_not_exist(self, group):
        member = Student(5, "Mary")
        expected = False

        result = member in group

        assert expected == result

    def test_contain_method_should_return_False_if_list_is_empty(self, group_empty):
        member = Student(1, "John")
        expected = False

        result = member in group_empty

        assert expected == result

    def test_str_method_should_return_name_of_all_members(self, group, group_empty):
        expected_1 = "John,Mary,Simon"
        expected_2 = ""

        result_1 = str(group)
        result_2 = str(group_empty)

    def test_get_members_method_should_return_empty_list_if_no_members_exist(self, group_empty):

        expected = []

        result = group_empty.get_members()

        assert expected == result


    def test_get_members_method_should_return_list_of_all_members(self, group):
        expected = [member.id for member in group._members]

        result = [member.id for member in group.get_members()]

        assert expected == result


    def test_get_members_method_should_return_list_of_all_members_as_shallow_copy(self, group):

        expected = [id(member) for member in group._members]

        result = [id(member) for member in group.get_members()]

        assert expected == result


"""
Task 8 - Grouping Classes
"""

class TestGrouping:
    def test_len_method_should_return_correct_value(self, grouping):

        expected = 2

        result = len(grouping)

        assert expected == result


    def test_str_method_should_return_name_of_all_members_in_all_group(self, grouping):

        expected = "John,Mary,Simon\nNanny,Dilbert,Jason"

        result = str(grouping)

        assert expected == result


    def test_add_group_method_should_return_False_if_same_student_is_in_more_than_one_group(self, grouping):
        group = Group([Student(1, "John"), Student(7, "Johnathan"), Student(8, "Nash")])
        expected = False

        result = grouping.add_group(group)

        assert expected == result

    def test_add_group_method_should_return_False_if_same_student_is_in_more_than_one_group(self, grouping):
        group = Group([Student(1, "John"), Student(8, "Johnathan"), Student(9, "Nash")])
        expected = False

        result = grouping.add_group(group)

        assert expected == result

    def test_add_group_method_should_return_correct_value_if_successful(self, grouping):
        group = Group([Student(7, "David"), Student(8, "Johnathan"), Student(9, "Nash")])
        expected = "John,Mary,Simon\nNanny,Dilbert,Jason\nDavid,Johnathan,Nash"

        grouping.add_group(group)

        result = str(grouping)

        assert expected == result

    def test_get_groups_method_should_return_shallow_copy_of_groups(self):
        group1 = Group([Student(1, "John"), Student(2, "Mary"), Student(3, "Simon")])
        group2 = Group([Student(4, "Nanny"), Student(5, "Dilbert"), Student(6, "Jason")])
        grouping = Grouping()
        grouping._groups = [group1, group2]

        expected = [id(group1), id(group2)]

        result = [id(group) for group in grouping.get_groups()]

        assert expected == result


"""
Task 9 - Survey Classes
"""

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

    def test_score_students_method_should_return_0_if_questions_dont_exist(self, students):
        survey = Survey([])

        expected = 0

        result = survey.score_students(students)

        assert expected == result

    def test_score_students_method_should_return_0_if_more_than_1_question_exists_but_answer_is_invalid(self, survey, students):
        questions = survey.get_questions()

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

        for question in mc_questions:
            for student in students:
                answer = Answer("A")
                student.set_answer(question, answer)


        for question in mc_questions:
            if question.id == 1:
                students_2[0].set_answer(question,Answer("A"))
                students_2[1].set_answer(question,Answer("B"))
                students_2[2].set_answer(question,Answer("C"))
            elif question.id == 2:
                students_2[0].set_answer(question,Answer("A"))
                students_2[1].set_answer(question,Answer("B"))
                students_2[2].set_answer(question,Answer("C"))
            elif question.id == 3:
                students_2[0].set_answer(question,Answer("A"))
                students_2[1].set_answer(question,Answer("B"))
                students_2[2].set_answer(question,Answer("C"))
            elif question.id == 4:
                students_2[0].set_answer(question,Answer("A"))
                students_2[1].set_answer(question,Answer("B"))
                students_2[2].set_answer(question,Answer("C"))

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

        for question in mc_questions:
            if question.id == 1:
                students_2[0].set_answer(question,Answer("A"))
                students_2[1].set_answer(question,Answer("B"))
                students_2[2].set_answer(question,Answer("C"))
            elif question.id == 2:
                students_2[0].set_answer(question,Answer("A"))
                students_2[1].set_answer(question,Answer("B"))
                students_2[2].set_answer(question,Answer("C"))
            elif question.id == 3:
                students_2[0].set_answer(question,Answer("A"))
                students_2[1].set_answer(question,Answer("B"))
                students_2[2].set_answer(question,Answer("C"))
            elif question.id == 4:
                students_2[0].set_answer(question,Answer("A"))
                students_2[1].set_answer(question,Answer("B"))
                students_2[2].set_answer(question,Answer("C"))

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

        for question in mc_questions:
            if question.id == 1:
                students_2[0].set_answer(question,Answer("A"))
                students_2[1].set_answer(question,Answer("A"))
                students_2[2].set_answer(question,Answer("C"))
            elif question.id == 2:
                students_2[0].set_answer(question,Answer("A"))
                students_2[1].set_answer(question,Answer("A"))
                students_2[2].set_answer(question,Answer("C"))
            elif question.id == 3:
                students_2[0].set_answer(question,Answer("A"))
                students_2[1].set_answer(question,Answer("A"))
                students_2[2].set_answer(question,Answer("C"))
            elif question.id == 4:
                students_2[0].set_answer(question,Answer("A"))
                students_2[1].set_answer(question,Answer("A"))
                students_2[2].set_answer(question,Answer("C"))

        expected_1 = 1.0
        expected_2 = 0.0

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

        for question in mc_questions:
            if question.id == 1:
                students_2[0].set_answer(question,Answer("A"))
                students_2[1].set_answer(question,Answer("A"))
                students_2[2].set_answer(question,Answer("C"))
            elif question.id == 2:
                students_2[0].set_answer(question,Answer("A"))
                students_2[1].set_answer(question,Answer("A"))
                students_2[2].set_answer(question,Answer("C"))
            elif question.id == 3:
                students_2[0].set_answer(question,Answer("A"))
                students_2[1].set_answer(question,Answer("A"))
                students_2[2].set_answer(question,Answer("C"))
            elif question.id == 4:
                students_2[0].set_answer(question,Answer("A"))
                students_2[1].set_answer(question,Answer("A"))
                students_2[2].set_answer(question,Answer("C"))

        expected_1 = 1.0
        expected_2 = 0.0

        result_1 = survey.score_students(students)
        result_2 = survey.score_students(students_2)

        assert expected_1 == result_1
        assert expected_2 == result_2

    def test_score_grouping_method_should_return_0_if_grouping_has_no_groups(self, survey):
        grouping = Grouping()

        expected = 0.0

        result = survey.score_grouping(grouping)

        assert expected == result

    def test_score_grouping_method_should_return_correct_value_if_all_is_well_for_homogeneous_criterion(self, grouping, grouping_2, mc_questions):
        survey = Survey(mc_questions)

        for group in grouping.get_groups():
            students = group.get_members()
            for student in students:
                for question in mc_questions:
                    answer = Answer("A")
                    student.set_answer(question, answer)

        for group in grouping_2.get_groups():
            students = group.get_members()
            for question in mc_questions:
                if question.id == 1:
                    students[0].set_answer(question,Answer("A"))
                    students[1].set_answer(question,Answer("B"))
                    students[2].set_answer(question,Answer("C"))
                elif question.id == 2:
                    students[0].set_answer(question,Answer("A"))
                    students[1].set_answer(question,Answer("B"))
                    students[2].set_answer(question,Answer("C"))
                elif question.id == 3:
                    students[0].set_answer(question,Answer("A"))
                    students[1].set_answer(question,Answer("B"))
                    students[2].set_answer(question,Answer("C"))
                elif question.id == 4:
                    students[0].set_answer(question,Answer("A"))
                    students[1].set_answer(question,Answer("B"))
                    students[2].set_answer(question,Answer("C"))

        expected_1 = 1.0
        expected_2 = 0.0

        result_1 = survey.score_grouping(grouping)
        result_2 = survey.score_grouping(grouping_2)

        assert expected_1 == result_1
        assert expected_2 == result_2

    def test_score_grouping_method_should_return_correct_value_if_all_is_well_for_hetrogeneous_criterion(self, grouping, grouping_2, mc_questions):
        survey = Survey(mc_questions)

        for group in grouping.get_groups():
            students = group.get_members()
            for student in students:
                for question in mc_questions:
                    answer = Answer("A")
                    survey.set_criterion(HeterogeneousCriterion(), question)
                    student.set_answer(question, answer)

        for group in grouping_2.get_groups():
            students = group.get_members()
            for question in mc_questions:
                if question.id == 1:
                    students[0].set_answer(question,Answer("A"))
                    students[1].set_answer(question,Answer("B"))
                    students[2].set_answer(question,Answer("C"))
                elif question.id == 2:
                    students[0].set_answer(question,Answer("A"))
                    students[1].set_answer(question,Answer("B"))
                    students[2].set_answer(question,Answer("C"))
                elif question.id == 3:
                    students[0].set_answer(question,Answer("A"))
                    students[1].set_answer(question,Answer("B"))
                    students[2].set_answer(question,Answer("C"))
                elif question.id == 4:
                    students[0].set_answer(question,Answer("A"))
                    students[1].set_answer(question,Answer("B"))
                    students[2].set_answer(question,Answer("C"))

        expected_1 = 0.0
        expected_2 = 1.0

        result_1 = survey.score_grouping(grouping)
        result_2 = survey.score_grouping(grouping_2)

        assert expected_1 == result_1
        assert expected_2 == result_2

    def test_score_grouping_method_should_return_correct_value_if_all_is_well_for_lonely_member_criterion(self, grouping, grouping_2, mc_questions):
        survey = Survey(mc_questions)

        for group in grouping.get_groups():
            students = group.get_members()
            for student in students:
                for question in mc_questions:
                    answer = Answer("A")
                    survey.set_criterion(LonelyMemberCriterion(), question)
                    student.set_answer(question, answer)

        for group in grouping_2.get_groups():
            students = group.get_members()
            for question in mc_questions:
                if question.id == 1:
                    students[0].set_answer(question,Answer("A"))
                    students[1].set_answer(question,Answer("A"))
                    students[2].set_answer(question,Answer("C"))
                elif question.id == 2:
                    students[0].set_answer(question,Answer("A"))
                    students[1].set_answer(question,Answer("A"))
                    students[2].set_answer(question,Answer("C"))
                elif question.id == 3:
                    students[0].set_answer(question,Answer("A"))
                    students[1].set_answer(question,Answer("A"))
                    students[2].set_answer(question,Answer("C"))
                elif question.id == 4:
                    students[0].set_answer(question,Answer("A"))
                    students[1].set_answer(question,Answer("A"))
                    students[2].set_answer(question,Answer("C"))

        expected_1 = 1.0
        expected_2 = 0.0

        result_1 = survey.score_grouping(grouping)
        result_2 = survey.score_grouping(grouping_2)

        assert expected_1 == result_1
        assert expected_2 == result_2


"""
Task 10 - Helper Functions
"""

class TestSliceListFunction:
    def test_function_should_return_empty_if_lst_has_length_0(self, lst_empty):
        expected = []

        result = slice_list(lst_empty, 0)

        assert expected == result

    def test_function_should_return_correct_value_if_successful(self, lst_1, lst_2):
        expected_1 = [[3, 4], [6, 2], [3]]
        expected_2 = [['a', 1, 6.0], [False]]

        result_1 = slice_list(lst_1, 2)
        result_2 = slice_list(lst_2, 3)

        assert expected_1 == result_1
        assert expected_2 == result_2

class TestWindowFunction:
    def test_function_should_return_empty_if_lst_has_length_0(self, lst_empty):
        expected = []

        result = windows(lst_empty, 0)

        assert expected == result

    def test_function_should_return_correct_value_if_successful(self, lst_1, lst_2):
        expected_1 = [[3, 4], [4, 6], [6, 2], [2, 3]]
        expected_2 = [['a', 1, 6.0], [1, 6.0, False]]

        result_1 = windows(lst_1, 2)
        result_2 = windows(lst_2, 3)

        assert expected_1 == result_1
        assert expected_2 == result_2


"""
Task 11 - Grouper Classes
"""


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
        expected = "Jason,Simon\nMary,Jessie"
        result = str(GreedyGrouper(2).make_grouping(course, survey))

        assert expected == result


class TestWindowsGrouper:
    def test_make_grouping_method_should_return_grouping_with_each_group_in_decreasing_students_score(self, course, survey, students_lst):

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
        expected = "Jason,Mary\nSimon,Jessie"
        result = str(WindowGrouper(2).make_grouping(course, survey))

        assert expected == result

if __name__ == '__main__':
    pytest.main(['tests.py'])
