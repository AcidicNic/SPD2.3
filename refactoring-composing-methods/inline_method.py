# by Kami Bigdely
# Inline method.
"""Checks if a person is of age."""

LEGAL_DRINKING_AGE = 18

class Person:
    """Represents a person."""
    def __init__(self, my_age):
        self.age = my_age


def enter_night_club(individual):
    """Checks if 'individual' is of age."""
    if individual.age >= LEGAL_DRINKING_AGE:
        print("Allowed to enter.")
    else:
        print("Enterance of minors is denited.")

if __name__ == '__main__':
    TEST_MINOR = Person(17.9)
    TEST_ADULT = Person(18)
    enter_night_club(TEST_MINOR)
    enter_night_club(TEST_ADULT)
