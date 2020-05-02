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

@pytest.fixture
def lst_empty() -> List:
    return []

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