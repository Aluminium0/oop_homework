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
