from Teacher import Teacher
from Student import Student

class Course:
    def __init__(self, course_name: str, teacher: Teacher) -> None:
        self.course_name = course_name
        self.teacher = teacher
        self.students = list()

    def enroll_student(self, student: Student):
        self.students.append(student)