# TODO: put all your tests in this file (you can delete this line)

import pytest
import unittest
from typing import List
from grouper import slice_list, windows

@pytest.fixture
def lst_1() -> List:
    return [3, 4, 6, 2, 3]

@pytest.fixture
def lst_2() -> List:
    return ['a', 1, 6.0, False]

class TestSliceListFunction:
    def test_function_should_return_empty_if_lst_has_length_0(self):
        lst = []
        expected = []

        result = slice_list(lst, 0)

        assert expected == result

    def test_function_should_return_correct_value_if_successful(self, lst_1, lst_2):
        expected_1 = [[3, 4], [6, 2], [3]]
        expected_2 = [['a', 1, 6.0], [False]]

        result_1 = slice_list(lst_1, 2)
        result_2 = slice_list(lst_2, 3)

        assert expected_1 == result_1
        assert expected_2 == result_2

