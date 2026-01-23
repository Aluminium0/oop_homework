def average_grade(grades: dict) -> float:
    all_grades = []
    for grade_list in grades.values():
        all_grades.extend(grade_list)
    return sum(all_grades) / len(all_grades) if all_grades else 0


class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecture(self, lecturer, course, grade):
        if (
            isinstance(lecturer, Lecturer)
            and course in self.courses_in_progress
            and course in lecturer.courses_attached
            and 1 <= grade <= 10
        ):
            lecturer.grades.setdefault(course, []).append(grade)
        else:
            return 'Ошибка'

    def __str__(self):
        return (
            f"Имя: {self.name}\n"
            f"Фамилия: {self.surname}\n"
            f"Средняя оценка за домашние задания: {average_grade(self.grades):.1f}\n"
            f"Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\n"
            f"Завершенные курсы: {", ".join(self.finished_courses)}"
        )

    def __lt__(self, other):
        return average_grade(self.grades) < average_grade(other.grades)

    def __eq__(self, other):
        return average_grade(self.grades) == average_grade(other.grades)


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def __str__(self):
        return (
            f"Имя: {self.name}\n"
            f"Фамилия: {self.surname}\n"
            f"Средняя оценка за лекции: {average_grade(self.grades):.1f}"
        )

    def __lt__(self, other):
        return average_grade(self.grades) < average_grade(other.grades)

    def __eq__(self, other):
        return average_grade(self.grades) == average_grade(other.grades)


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if (
            isinstance(student, Student)
            and course in self.courses_attached
            and course in student.courses_in_progress
            and 1 <= grade <= 10
        ):
            student.grades.setdefault(course, []).append(grade)
        else:
            return "Ошибка"

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}"


#  Testing (Task 4)

student1 = Student("Anna", "Ivanova", "F")
student2 = Student("Max", "Petrov", "M")

lecturer1 = Lecturer("Ivan", "Ivanov")
lecturer2 = Lecturer("Sergey", "Smirnov")

reviewer1 = Reviewer("Petr", "Petrov")
reviewer2 = Reviewer("Olga", "Sidorova")

student1.courses_in_progress += ["Python"]
student2.courses_in_progress += ["Python"]

lecturer1.courses_attached += ["Python"]
lecturer2.courses_attached += ["Python"]

reviewer1.courses_attached += ["Python"]
reviewer2.courses_attached += ["Python"]

reviewer1.rate_hw(student1, "Python", 9)
reviewer1.rate_hw(student2, "Python", 8)
reviewer2.rate_hw(student1, "Python", 10)
reviewer2.rate_hw(student2, "Python", 9)

student1.rate_lecture(lecturer1, "Python", 8)
student1.rate_lecture(lecturer2, "Python", 9)
student2.rate_lecture(lecturer1, "Python", 9)
student2.rate_lecture(lecturer2, "Python", 10)

print(student1)
print(student2)
print(lecturer1)
print(lecturer2)
print(reviewer1)
print(reviewer2)

print(average_hw_grade([student1, student2], "Python"))
print(average_lecture_grade([lecturer1, lecturer2], "Python"))
