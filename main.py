# # Задача 1
#
# class Student:
#     def __init__(self, name, surname, gender):
#         self.name = name
#         self.surname = surname
#         self.gender = gender
#         self.finished_courses = []
#         self.courses_in_progress = []
#         self.grades = {}
#
#
# class Mentor:
#     def __init__(self, name, surname):
#         self.name = name
#         self.surname = surname
#         self.courses_attached = []
#
#     def rate_hw(self, student, course, grade):
#         if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
#             if course in student.grades:
#                 student.grades[course] += [grade]
#             else:
#                 student.grades[course] = [grade]
#         else:
#             return 'Ошибка'
# class Lecturer(Mentor):
#     pass
# class Reviewer(Mentor):
#     pass
#
# best_student = Student('Ruoy', 'Eman', 'your_gender')
# best_student.courses_in_progress += ['Python']
#
# cool_mentor = Mentor('Some', 'Buddy')
# cool_mentor.courses_attached += ['Python']
#
# cool_mentor.rate_hw(best_student, 'Python', 10)
# cool_mentor.rate_hw(best_student, 'Python', 10)
# cool_mentor.rate_hw(best_student, 'Python', 10)
#
# print(best_student.grades)

# Задача 2

class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecture(self, lecturer, course, grade):
        if isinstance(lecturer,
                      Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    grades = {}


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


best_lecturer = Lecturer('Some', 'Man')
best_lecturer.courses_attached += ['Python']

best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']

best_student.rate_lecture(best_lecturer, 'Python', 10)
best_student.rate_lecture(best_lecturer, 'Python', 9)
best_student.rate_lecture(best_lecturer, 'Python', 9)

cool_reviewer = Reviewer('Some', 'Buddy')
cool_reviewer.courses_attached += ['Python']

cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 10)

print(f"Оценки лучшего студента: {best_student.grades}")
print(f"Оценки лучшего лектора, выставленные лучшим студентом: {best_lecturer.grades}")


# Задача 3

class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.average_value = []

    def rate_lecture(self, lecturer, course, grade):
        if isinstance(lecturer,
                      Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def get_average_student_rating(self, students_grades):
        for student in students_grades.values():
            avg_val = sum(student) / len(student)
            self.average_value = avg_val

    def __str__(self):
        return f"\nИмя студента: {self.name}\nФамилия студента: {self.surname}\nСредняя оценка за ДЗ от проверяющего: {self.average_value}\nКурсы в процессе изучения: {', '.join(self.courses_in_progress)}\nЗавершенные курсы: {', '.join(self.finished_courses)}"

    def __lt__(self, other):
        return self.average_value < other.average_value


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        Mentor.__init__(self, name, surname)
        self.grades = {}
        self.average = []

    def get_average_lecturer_rating(self, lecturers_grades):
        for lecturer in lecturers_grades.values():
            avg_val = sum(lecturer) / len(lecturer)
            self.average = avg_val

    def __str__(self):
        return f"\nИмя лектора: {self.name}\nФамилия лектора: {self.surname}\nСредняя оценка за лекции: {self.average}"

    def __lt__(self, other):
        return self.average < other.average


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f"\nИмя проверяющего: {self.name}\nФамилия проверяющего: {self.surname}"


first_Lecturer = Lecturer('Rudolf', 'Schenker')
first_Lecturer.courses_attached += ['Python', 'Git']

second_Lecturer = Lecturer('Klaus', 'Meine')
second_Lecturer.courses_attached += ['Python', 'Git']

first_student = Student('Anthony ', 'Kiedis', 'your_gender')
first_student.courses_in_progress += ['Python', 'Git']
first_student.finished_courses += ['Введение в программирование']

second_student = Student('John', 'Frusciante', 'your_gender')
second_student.courses_in_progress += ['Python', 'Git']
second_student.finished_courses += ['Введение в программирование']

first_Reviewer = Reviewer('Chad', 'Kroeger')
first_Reviewer.courses_attached += ['Python', 'Git']

second_Reviewer = Reviewer('Ryan', 'Peake')
second_Reviewer.courses_attached += ['Python', 'Git']

first_student.rate_lecture(first_Lecturer, 'Python', 10)
first_student.rate_lecture(first_Lecturer, 'Python', 9)
first_student.rate_lecture(first_Lecturer, 'Python', 9)

second_student.rate_lecture(second_Lecturer, 'Python', 10)
second_student.rate_lecture(second_Lecturer, 'Python', 9)
second_student.rate_lecture(second_Lecturer, 'Python', 7)

first_student.rate_lecture(first_Lecturer, 'Git', 7)
first_student.rate_lecture(first_Lecturer, 'Git', 8)
first_student.rate_lecture(first_Lecturer, 'Git', 9)

second_student.rate_lecture(second_Lecturer, 'Git', 9)
second_student.rate_lecture(second_Lecturer, 'Git', 5)
second_student.rate_lecture(second_Lecturer, 'Git', 7)

first_Reviewer.rate_hw(first_student, 'Python', 10)
first_Reviewer.rate_hw(first_student, 'Python', 10)
first_Reviewer.rate_hw(first_student, 'Python', 10)

second_Reviewer.rate_hw(second_student, 'Python', 10)
second_Reviewer.rate_hw(second_student, 'Python', 10)
second_Reviewer.rate_hw(second_student, 'Python', 7)

first_Reviewer.rate_hw(first_student, 'Git', 8)
first_Reviewer.rate_hw(first_student, 'Git', 10)
first_Reviewer.rate_hw(first_student, 'Git', 9)

second_Reviewer.rate_hw(second_student, 'Git', 6)
second_Reviewer.rate_hw(second_student, 'Git', 9)
second_Reviewer.rate_hw(second_student, 'Git', 9)

first_student.get_average_student_rating(first_student.grades)
second_student.get_average_student_rating(second_student.grades)
first_Lecturer.get_average_lecturer_rating(first_Lecturer.grades)
second_Lecturer.get_average_lecturer_rating(second_Lecturer.grades)

print(first_Reviewer)
print(second_Reviewer)
print(first_Lecturer)
print(second_Lecturer)

print(first_student)
print(second_student)

print(first_student.average_value > second_student.average_value)

print(first_Lecturer.average < second_Lecturer.average)

students_list = [first_student, second_student]
lecturers_list = [first_Lecturer, second_Lecturer]


# Задача 4

def get_average_students_grade(students, course):
    total = []
    for student in students:
        total.append(sum(student.grades[course]) / len(student.grades[course]))
    print(f'Средняя оценка студентов по курсу {course}: {sum(total) / len(total)}')


def get_average_lecturers_grade(lecturers, course):
    total = []
    for lecturer in lecturers:
        total.append(sum(lecturer.grades[course]) / len(lecturer.grades[course]))
    print(f'Средняя оценка лекторов по курсу {course}: {sum(total) / len(total)}')


get_average_students_grade(students_list, 'Python')
get_average_students_grade(students_list, 'Git')

get_average_lecturers_grade(lecturers_list, 'Python')
get_average_lecturers_grade(lecturers_list, 'Git')
