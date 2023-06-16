
# Завдання №7. Створіть клас Student, який представляє студента. Реалізуйте атрибут класу для відстеження кількості
# студентів. Для цього змінюйте значення атрибута класу у методі __init__ . Та створіть клас метод для виведення
# загальної кількості студентів.

class Student:
    students = []
    count = 0

    def __init__(self, firstname, lastname, course):
        self.firstname = firstname
        self.lastname = lastname
        self.course = course

    def __repr__(self):
        return f'Студент {self.firstname} {self.lastname}, {self.course}-й курс'

    def __eq__(self, other):
        if isinstance(other, Student):
            return (
                    self.firstname == other.firstname
                    and self.lastname == other.lastname
                    and self.course == other.course
            )
        return False

    @classmethod
    def add_students(cls, *students):
        for student in students:
            if student not in cls.students:
                cls.students.append(student)
        cls.count = f'Кількість студентів: {len(cls.students)}'


student_1 = Student("John", "Smith", 2)
student_2 = Student("Emily", "Johnson", 3)
student_3 = Student("Michael", "Williams", 1)
student_4 = Student("Sophia", "Brown", 3)
student_5 = Student("Daniel", "Taylor", 4)
student_6 = Student("Olivia", "Anderson", 1)
student_7 = Student("Matthew", "Thomas", 2)
student_8 = Student("Ava", "Martinez", 3)
student_9 = Student("Ava", "Martinez", 3)

Student.add_students(
    student_1, student_2, student_3, student_4, student_5, student_6, student_7, student_8, student_9
)
print(Student.count)
