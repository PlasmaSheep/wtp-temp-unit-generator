"""Models for the temp unit generator.
"""

class Class(object):
    """This represents a class, composed of multiple units, which contain
    students. Students cannot be duplicated across units.
    """

    units = []

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
        """Add a student to a unit, checking to make sure this student does
        not already exist in another unit.

        Arguments:
            student (Student): A ``Student`` object to put into a unit.
            unit (int): Which unit to put this student in (0-indexed)

        Raises:
            ValueError: If this student is already in this Class.
        """
        if not self.student_exists(student):
            student.unit_mates.extend(self.units[unit].students)
            self.units[unit].append(student)
        else:
            raise ValueError("Student exists already in this Class.")

    def get_unit(self, number):
        """Get the unit with the correct number.
        """
        for unit in self.units:
            if unit.number == number:
                return unit
        raise ValueError("No such unit found")

    def __repr__(self):
        return "Class(units=%s)" % self.units

class Unit(object):
    """A unit contains several students.
    """

    max_students = 1
    students = []
    number = 0
    index = 0

    def __init__(self, max_students, number, students=[]):
        """Create a new ``Unit``.
        """
        self.students = []
        if students:
            self.students = students
        self.number = number
        self.max_students = max_students

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == len(self.students):
            raise StopIteration
        self.index += 1
        return self.students[self.index - 1]

    def append(self, item):
        """Add a new ``Student`` to this unit, making sure there aren't
        too many.

        Arguments:
            item (Student): The ``Student`` to add.

        Raises:
            ValueError: if ``max_students`` would be exceeded.
        """
        if len(self.students) < self.max_students:
            self.students.append(item)
        else:
            raise ValueError("Too many students in this unit.")

    def __repr__(self):
        return "Unit(max_students=%s, students=%s, number=%s)" % \
                (self.max_students, self.students, self.number)

class Student(object):
    """Represents a student in a class and in units.
    """

    name = ""
    unit_mates = []

    def __init__(self, name):
        """Instantiate a student.

        Arguments:
            name (str): The student's name.
        """
        self.name = name

    def __eq__(self, other):
        """Determine if two students are the same by their names.
        """
        if self.name == other.name:
            return True
        return False

    def __repr__(self):
        """Print the user's name.
        """
        return "Student(name=%s)" % self.name

