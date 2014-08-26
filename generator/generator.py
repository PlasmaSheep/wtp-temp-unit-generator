"""Temp unit generator.
"""

from .models import Class
from .models import Unit
from .models import Student

def get_unit_sizes(class_size, number_of_units):
    """Given a class size, determine the best unit sizing.

    Arguments:
        class_size (int): Number of students in the class.
    """

    base_size = int(class_size / number_of_units)
    remainder = class_size - base_size * number_of_units
    unit_sizes = []

    for i in range(0, number_of_units):
        if i < remainder:
            unit_sizes.append(base_size + 1)
        else:
            unit_sizes.append(base_size)

    unit_sizes.sort()

    return unit_sizes

class Generator(object):
    """The temp unit generator class.
    """
    def __init__(self, iterations, student_names, number_of_units):
        """Instantiate a temp unit generator.

        Arguments:
            class_size (int): Number of students in the class.
            iterations (int): How many temp units to go through.
            student_names (list of str): Names of the students.
        """

        self.class_size = len(student_names)
        self.students = []
        self.classes = []
        unit_sizes = get_unit_sizes(self.class_size, number_of_units)

        for i in range(0, iterations):
            new_class = Class(i)
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

        # Recurse
        self.assort_students(new_numbering, class_number + 1)

    def print_classes(self):
        """Print out the classes.
        """
        for temp_class in self.classes:
            print("Temp unit " + str(temp_class.number + 1))
            for unit in temp_class.units:
                print(" Group " + str(unit.number + 1))
                for student in unit.students:
                    print("  " + student.name)

