# TODO: put all your tests in this file (you can delete this line)

import pytest
import unittest
from course import Student
from grouper import Grouping, Group

@pytest.fixture
def grouping() -> Grouping:
    group1 = Group([Student(1, "John"), Student(2, "Mary"), Student(3, "Simon")])
    group2 = Group([Student(4, "Nanny"), Student(5, "Dilbert"), Student(6, "Jason")])

    grouping = Grouping()
    grouping._groups = [group1, group2]
    return grouping


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