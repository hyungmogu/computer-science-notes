# TODO: put all your tests in this file (you can delete this line)

import pytest
import unittest
from grouper import Grouping, Group

@pytest.fixture
def grouping() -> Grouping:
    group1 = Group([Student(1, "John"), Student(2, "Mary"), Student(3, "Simon")])
    group2 = Group([Student(4, "Nanny"), Student(5, "Dilbert"), Student(6, "Jason")])

    return Grouping([group1, group2])


class TestGrouping:

    def test_len_method_should_return_correct_value(self, grouping):

        expected = 2

        result = len(grouping)

        assert expected == result