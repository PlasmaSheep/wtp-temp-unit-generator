"""Temp unit generator.
"""

from .models import Class
from .models import Unit
from .models import Student

def get_unit_sizes(class_size):
    """Given a class size, determine the best unit sizing.

    Arguments:
        class_size (int): Number of students in the class.
    """

    base_size = int(class_size / 6)
    remainder = class_size - base_size * 6
    unit_sizes = []

    for i in range(0, 6):
        if i < remainder:
            unit_sizes.append(base_size + 1)
        else:
            unit_sizes.append(base_size)

    unit_sizes.sort()

    return unit_sizes

class Generator(object):
    """The temp unit generator class.
    """
    def __init__(self, class_size, iterations, student_names):
        """Instantiate a temp unit generator.

        Arguments:
            class_size (int): Number of students in the class.
            iterations (int): How many temp units to go through.
            student_names (list of str): Names of the students.
        """

        self.class_size = class_size
        self.students = []
        self.classes = []
        unit_sizes = get_unit_sizes(class_size)

        for i in range(0, iterations):
            new_class = Class()
            for i in range(0, len(unit_sizes)):
                new_class.units.append(Unit(unit_sizes[i], i))
            self.classes.append(new_class)

        for name in student_names:
            self.students.append(Student(name))

    def assort_students(self, numbering=[], class_number=0):
        """Assort the students into their units over several classes.
        """

        if class_number == len(self.classes):
            # We've iterated over every Class
            return

        if not numbering:
            # Create a numbering scheme
            for unit in self.classes[class_number].units:
                for i in range(0, unit.max_students):
                    numbering.append(unit.number)

        # Assort students based on the numbering scheme
        for student, assigned_unit in zip(self.students, numbering):
            self.classes[class_number].get_unit(assigned_unit).append(student)

        # Shift the numbering
        new_numbering = [numbering[-1]]
        for number in numbering[:-1]:
            new_numbering.append(number)

