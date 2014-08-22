"""Tests for the generator.
"""

import unittest
from unittest import mock

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

    @mock.patch("generator.generator.get_unit_sizes", autospec=True)
    @mock.patch("generator.generator.Class", autospec=True)
    @mock.patch("generator.generator.Unit", autospec=True)
    @mock.patch("generator.generator.Student", autospec=True)
    def test_constructor(self, mock_student, mock_unit, mock_class,
            mock_get_unit_sizes):
        """Test the constructor.
        """

        mock_get_unit_sizes.return_value = [2, 2, 3]
        gen = generator.Generator(10, 2, ["A", "B"])

        class1 = mock_class()
        class2 = mock_class()
        class1.units = [mock_unit(2, 0), mock_unit(2, 1), mock_unit(3, 2)]
        class2.units = [mock_unit(2, 0), mock_unit(2, 1), mock_unit(3, 2)]


        assert gen.class_size == 10
        assert gen.students == [mock_student("A"), mock_student("B")]
        assert gen.classes == [class1, class2]

    def test_assort_students(self):
        """Test assorting students.
        """
        student_names = [str(i) for i in range(0, 10)]
        gen = generator.Generator(10, 2, student_names)

        gen.assort_students()

