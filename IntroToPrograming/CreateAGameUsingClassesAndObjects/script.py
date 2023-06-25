from Student import Student
from Teacher import Teacher
from Course import Course

studentA = Student("John Doe", 17, 11)
teacherA = Teacher("Jane Aaron", "Mrs.")
courseA = Course("Computer Science", teacherA, "9AM", "11AM")

print(studentA)
print(teacherA)
print(courseA)