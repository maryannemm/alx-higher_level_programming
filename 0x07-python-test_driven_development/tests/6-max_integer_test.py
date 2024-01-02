#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
from parameterized import parameterized
from typing import List
from max_integer import max_integer

class TestMaxInteger(unittest.TestCase):

    @parameterized.expand([
        ([1, 2, 3, 4], 4),
        ([1, 3, 4, 2], 4),
        ([], None),
        ([5], 5),
        ([-1, -2, -3, -4], -1),
        ([-1, -3, -4, -2], -1),
        ([-1, -3, -4, 0], 0),
    ])
    def test_max_integer(self, input_list: List[int], expected_result: int):
        result = max_integer(input_list)
        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()

