# By Kamran Bigdely Nov. 2020
# Replace temp variable with query

"""
Finds graduating students and sends students' contact info possible employers.
"""

class Employer:
    """Represents an employer."""
    def __init__(self, name):
        self.name = name

    def send(self, students):
        """Sends 'students' contact into to the employer."""
        print(f"Students' contact info were sent to {self.name}.")

class Student:
    """Represents a student."""
    def __init__(self, gpa, name):
        self.gpa = gpa
        self.name = name

    def get_gpa(self):
        """Returns the student's gpa."""
        return self.gpa

    def send_congrat_email(self):
        """Sends graduation email to the student."""
        print(f"Congrats {self.name}. You graduated successfully!")

class School:
    """Represents a school."""
    def __init__(self, students) -> None:
        self.students = students

    def get_passing_students(self, min_gpa=2.5):
        """Returns a list of students with a gpa greater than 'min_gpa'."""
        passed_students = []

        for student in self.students:
            if student.get_gpa() > min_gpa:
                passed_students.append(student)
        return passed_students

    def email_passing_students(self):
        """Emails all graduating students."""
        for student in self.get_passing_students():
            student.send_congrat_email()

    def print_pretty_student_list(self, title, students):
        """Prints a list of students."""
        print(f"*** {title} ***")

        for student in students:
            print(student.name)

        print('*' * (len(title) + 8))

    def get_top_10_percent_students(self):
        """Returns list of top 10% of passing students sorted by gpa."""
        passed_students = self.get_passing_students()
        passed_students.sort(key=lambda s: s.get_gpa())
        index = int(0.9 * len(passed_students))
        return passed_students[index:]

    def email_top_employers(self):
        """Sends top 10 percent students contact info to the top employers."""
        top_employers = [
            Employer('Microsoft'),
            Employer('Free Software Foundation'),
            Employer('Google')
        ]
        for employer in top_employers:
            employer.send(self.get_top_10_percent_students())

    def process_graduation(self):
        """Find the students in the school who have successfully graduated."""
        self.print_pretty_student_list("Graduated Students",
                                        self.get_passing_students())

        self.email_passing_students()

        self.email_top_employers()



if __name__ == '__main__':
    TEST_STUDENTS = [Student(2.1, 'donald'), Student(2.3, 'william'),
                    Student(2.7, 'toro'),Student(3.9, 'lili'),
                    Student(3.2,'kami'), Student(3,'sarah')]
    TEST_SCHOOL  = School(TEST_STUDENTS)
    TEST_SCHOOL.process_graduation()
