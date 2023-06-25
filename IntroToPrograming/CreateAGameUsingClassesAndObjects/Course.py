from Teacher import Teacher
from Student import Student

class Course:
    def __init__(self, course_name: str, teacher: Teacher, start_time, end_time) -> None:
        self.course_name = course_name
        self.teacher = teacher
        self.start_time = start_time
        self.end_time = end_time
        self.students = list()
        teacher.add_course(self.course_name)

    def __repr__(self):
        return "{} taught by {} from {} to {}".format(self.course_name, self.teacher.name, self.start_time, self.end_time)

    def enroll_student(self, student: Student):
        self.students.append(student)