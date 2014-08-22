"""Models for the temp unit generator.
"""

class Class(object):
    """This represents a class, composed of multiple units, which contain
    students. Students cannot be duplicated across units.
    """

    def __init__(self):
        self.units = []

    def student_exists(self, student):
        """Check if a student is already in a unit.

        Arguments:
            student (Student): The student to add.

        Returns:
            ``True`` if the student is in a unit, ``False`` otherwise.
        """
        for unit in self.units:
            if student in unit:
                return True
        return False

    def add_student(self, student, unit):
        if not self.student_exists(student):
            student.unit_mates.extend(self.units[unit].students)
            self.units[unit].append(student)
        else:
            raise ValueError("Student exists already in this class.")

class Unit(object):
    """A unit contains several students.
    """
    def __init__(self, max_students):
        self.max_students = max_students
        self.students = []
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == len(self.students):
            raise StopIteration
        self.index += 1
        return self.students[self.index - 1]

    def append(self, item):
        if len(self.students) < self.max_students:
            self.students.append(item)
        else:
            raise ValueError("Too many students in this unit.")

class Student(object):
    """Represents a student in a class and in units.
    """
    def __init__(self, name):
        """Instantiate a student.

        Arguments:
            name (str): The student's name.
        """
        self.name = name
        self.unit_mates = []

    def __eq__(self, other):
        """Determine if two students are the same by their names.
        """
        if self.name == other.name:
            return True
        return False

