"""Run the generator interactively.
"""

from generator.generator import Generator
import pdb
def get_coerced_input(message, coerce):
    """Get input that coerces into a certain data type.
    """
    while True:
        text = input(message + " ")
        try:
            return coerce(text)
        except ValueError:
            continue

def get_input_list(message):
    input_list = []
    while True:
        text = input(message + " " + str(len(input_list) + 1) + ": ")
        if str(text):
            input_list.append(text)
        else:
            return input_list

def generate_interactively():
    print("Welcome to the temp unit generator.")
    print()

    iterations = get_coerced_input("How many total units will the class go "
        "through?", int)
    print()

    print("Enter the names of the students, hitting enter after every name.")
    print("Press enter without writing anything to stop adding students.")
    print()

    student_names = get_input_list("Student")
    print()

    number_of_units = get_coerced_input("How many different units are there?",
        int)
    print()

    print("Okay, generating class.")
    print()

    generator = Generator(iterations, student_names, number_of_units)
    generator.assort_students()

    print("Here's how to assign the students:")
    print()

    generator.print_classes()

    print()
    print("You should save this list for future use.")

if __name__ == "__main__":
    generate_interactively()

