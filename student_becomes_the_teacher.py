"""
a_student_becomes_teacher
"""
def func():
    """
    main function
    """
    lloyd = {
        "name": "Lloyd",
        "homework": [90.0, 97.0, 75.0, 92.0],
        "quizzes": [88.0, 40.0, 94.0],
        "tests": [75.0, 90.0]
        }
    alice = {
        "name": "Alice",
        "homework": [100.0, 92.0, 98.0, 100.0],
        "quizzes": [82.0, 83.0, 91.0],
        "tests": [89.0, 97.0]
        }
    tyler = {
        "name": "Tyler",
        "homework": [0.0, 87.0, 75.0, 22.0],
        "quizzes": [0.0, 75.0, 78.0],
        "tests": [100.0, 100.0]
        }
    students = [lloyd, alice, tyler]
    def average(numbers):
        """
        average
        """
        total = float(sum(numbers))
        return float(total) / len(numbers)
    def get_average(student):
        """
        get_average
        """
        homework = average(student["homework"])
        quizzes = average(student["quizzes"])
        tests = average(student["tests"])
        return (homework * .10) + (quizzes * .30) + (tests * .60)
    def get_letter_grade(score):
        """
        get_letter_grade
        """
        if score >= 90:
            return "A"
        elif score >= 80:
            return "B"
        elif score >= 70:
            return "C"
        elif score >= 60:
            return "D"
        else:
            return "F"
    def get_class_average(students):
        """
        get_class_average
        """
        results = []
        for student in students:
            student['average'] = get_average(student)
            student['letter_grade'] = get_letter_grade(student['average'])
            results.append(get_average(student))
        return average(results)
    def print_all_students(students):
        """
        prints all students
        """
        for student in students:
            for key in student:
                print  '{0}: {1}'.format(key, student[key])
            print '\n'
    print 'class average: {:.2f}\n'.format(get_class_average(students))
    print_all_students(students)
func()
