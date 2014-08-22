"""Tests for the generator.
"""

import unittest

from generator import generator
import pdb

class TestGenerator(unittest.TestCase):
    def test_get_unit_sizes(self):
        test_data = {26: [4, 4, 4, 4, 5, 5],
            27: [4, 4, 4, 5, 5, 5],
            24: [4, 4, 4, 4, 4, 4]}
        for size, result in test_data.items():
            print("Testing with " + str(size))
            assert generator.get_unit_sizes(size) == result

