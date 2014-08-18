"""Temp unit generator.
"""

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

