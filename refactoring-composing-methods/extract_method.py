# Written by Kamran Bigdely
# Example for Compose Methods: Extract Method.
"""
Takes in 5 student's grades, prints the mean and standard deviation.
"""

import math

def get_grade_inputs(n_student=5):
    """Returns a list of grades with the length of 'n_student'."""
    grade_list = []
    for i in range(0, n_student):
        grade_list.append(int(input(f"Enter grade for student {i+1}: ")))
    print()
    return grade_list

def get_mean(grade_list):
    """Returns the mean of 'grade_list'."""
    return sum(grade_list) / len(grade_list)

def get_std_dev(grade_list, grade_mean=None):
    """Returns the standard deviation of 'grade_list'."""
    if grade_mean is None:
        grade_mean = get_mean(grade_list)
    sum_of_sqrs = 0

    for grade in grade_list:
        sum_of_sqrs += (grade - grade_mean) ** 2

    return math.sqrt(sum_of_sqrs / len(grade_list))

def print_title(title):
    """Prints 'title' with 6 stars on either end."""
    print(f"****** {title} ******")

def print_summary(grade_mean, std_dev):
    """Prints 'grade_mean' and 'std_dev' with title banners."""
    print_title("Grade Statistics")
    print(f"The grades's mean is: {grade_mean:.1f}")
    print(f"The population standard deviation of grades is: {std_dev:.3f}")
    print_title("END")

def print_results():
    """Gets and prints grade list, std_dev, and mean."""
    grade_list = get_grade_inputs()
    grade_mean = get_mean(grade_list)
    std_dev = get_std_dev(grade_list, grade_mean)

    print_summary(grade_mean, std_dev)


if __name__ == '__main__':
    print_results()
