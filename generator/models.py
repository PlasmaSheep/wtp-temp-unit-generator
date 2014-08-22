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
            student.unit_mates.extend(self.units[unit])
            self.units[unit].append(student)
        else:
            raise ValueError("Student exists already in this class.")

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

