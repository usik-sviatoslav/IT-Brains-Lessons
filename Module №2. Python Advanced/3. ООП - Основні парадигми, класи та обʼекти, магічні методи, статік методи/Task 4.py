
# Завдання №4. Створіть клас Student для представлення студента. Додайте атрибути, такі як ім'я, прізвище і
# список оцінок. Реалізуйте метод __len__, який повертає кількість оцінок студента. Створіть список студентів і
# відсортуйте його за кількістю оцінок.

class Student:
    def __init__(self, firstname, lastname, grades):
        self.firstname = firstname
        self.lastname = lastname
        self.grades = grades

    def __len__(self):
        return len(self.grades)

    def __repr__(self):
        grades = ", ".join([str(grade) for grade in self.grades])
        return f"{self.firstname} {self.lastname}.\nОцінки: {grades}\n"

    @staticmethod
    def students(*students):
        students_list = list(students)
        students_list.sort(key=lambda student: len(student.grades))
        result = "\n".join([repr(student) for student in students_list])
        return result


student_1 = Student("John", "Smith", [78, 89, 67, 95, 92])
student_2 = Student("Emily", "Johnson", [82, 91, 75, 88])
student_3 = Student("Michael", "Williams", [90, 85, 79, 93, 87])
student_4 = Student("Sophia", "Brown", [95, 88, 91, 86])
student_5 = Student("Daniel", "Taylor", [79, 83, 90, 92, 84, 88])
student_6 = Student("Olivia", "Anderson", [87, 92, 84, 79])
student_7 = Student("Matthew", "Thomas", [91, 85, 88, 92, 90])
student_8 = Student("Ava", "Martinez", [88, 90, 82, 86])
student_9 = Student("David", "Harris", [84, 78, 80, 89, 82])
student_10 = Student("Emma", "Clark", [92, 87, 89, 91, 86])

print(student_1.__len__())
print(student_2.__len__())
print(student_3.__len__())
print(student_4.__len__())
print(student_5.__len__())
print()
print(Student.students(
    student_1, student_2, student_3, student_4, student_5, student_6, student_7, student_8, student_9, student_10)
)
