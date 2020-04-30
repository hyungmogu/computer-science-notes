# TODO: put all your tests in this file (you can delete this line)

import pytest
import unittest
from grouper import Group
from course import Student

@pytest.fixture
def group() -> Group:
    return Group([Student(1, "John"), Student(2, "Mary"), Student(3, "Simon")])

@pytest.fixture
def group_empty() -> Group:
    return Group([])


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
