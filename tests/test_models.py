"""Tests for the models.
"""
import unittest

from generator.models import Class
from generator.models import Student
from generator.models import Unit

class TestClass(unittest.TestCase):
    """Tests for the Class model.
    """
    def setUp(self):
        self.class_object = Class()
        unit1 = Unit(2, 1)
        unit2 = Unit(2, 2)
        unit1.students = [Student("a"), Student("b")]
        unit2.students = [Student("c")]
        self.class_object.units = [unit1, unit2]

    def test_student_exists(self):
        """Check student_exists.
        """
        assert self.class_object.student_exists(Student("c"))
        assert not self.class_object.student_exists(Student("f"))

    def test_add_existing_student(self):
        """See if we can add an existing student.
        """
        self.assertRaises(ValueError, self.class_object.add_student,
            Student("a"), 1)

    def test_add_new_student(self):
        """See if we can add a nonexistant student.
        """
        new_student = Student("foo")

        self.class_object.add_student(new_student, 1)

        assert new_student in self.class_object.units[1]
        assert new_student.unit_mates == [Student("c")]

class TestUnit(unittest.TestCase):
    """Tests for the Unit model.
    """
    def setUp(self):
        self.unit = Unit(5, 0)

    def test_append(self):
        """Make sure there's a limit to how much we can append
        """
        for i in range(0, self.unit.max_students):
            self.unit.append(i)

        self.assertRaises(ValueError, self.unit.append, 2)

class TestStudent(unittest.TestCase):
    """Tests for the Student model.
    """
    def setUp(self):
        self.student = Student("foo")

    def test_eq(self):
        """Make sure equality works.
        """
        student2 = Student("foo")
        student2.unit_mates = [Student("f"), Student("e")]
        student3 = Student("bar")

        assert student2 == self.student
        assert student3 != self.student

    def test_print(self):
        """Make sure printing works.
        """
        assert "foo" in str(self.student)

