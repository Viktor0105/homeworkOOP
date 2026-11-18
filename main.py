class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def average_grade(self):
        all_grades = []
        for grade in self.grades.values():
            for g in grade:
                all_grades.append(g)
        return round(sum(all_grades)/len(all_grades), 1) if all_grades else 0.0

    def __gt__(self, other):
        return self.average_grade() > other.average_grade()

    def __lt__(self, other):
        return self.average_grade() < other.average_grade()

    def __eq__(self, other):
        return self.average_grade() == other.average_grade()

    def __str__(self):
        return (f'Имя: {self.name}\n'
                f'Фамилия: {self.surname}\n'
                f'Средняя оценка за лекции: {self.average_grade()}')

class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
    def __str__(self):
        return (f'Имя: {self.name}\n'
                f'Фамилия: {self.surname}')

class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def average_grade(self):
        all_grades = []
        for grade in self.grades.values():
            for g in grade:
                all_grades.append(g)
        return round(sum(all_grades)/len(all_grades), 1) if all_grades else 0.0

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __gt__(self, other):
        return self.average_grade() > other.average_grade()

    def __lt__(self, other):
        return self.average_grade() < other.average_grade()

    def __eq__(self, other):
        return self.average_grade() == other.average_grade()

    def __str__(self):
        return (f'Имя: {self.name}\n'
                f'Фамилия: {self.surname}\n'
                f'Средняя оценка за домашние задания: {self.average_grade()}\n'
                f'Курсы в процессе изучения: {" ,".join(self.courses_in_progress)}\n'
                f'Завершенные курсы: {" ,".join(self.finished_courses)}')

def average_grade_all_lecturers(lecturers, course):
    all_grades = []
    for lecturer in lecturers:
        if isinstance(lecturer, Lecturer) and course in lecturer.grades:
            all_grades += lecturer.grades[course]
    return round(sum(all_grades)/len(all_grades), 1) if all_grades else 0.0

def average_grade_all_students(students, course):
    all_grades = []
    for student in students:
        if isinstance(student, Student) and course in student.grades:
            all_grades += student.grades[course]
    return round(sum(all_grades)/len(all_grades), 1) if all_grades else 0.0





best_student = Student('Иван', 'Иванов', 'male')
best_student.finished_courses += ['Git', 'Java']
best_student.courses_in_progress += ['Python']
best_student.grades['Git'] = [10, 10, 9, 10, 9]
best_student.grades['Java'] = [10, 8, 10, 9, 9]
best_student.grades['Python'] = [9, 10, 10]

second_student = Student('Пётр', 'Петров', 'male')
second_student.finished_courses += ['Git']
second_student.courses_in_progress += ['Python']
second_student.grades['Git'] = [8, 7, 7, 8, 9]
second_student.grades['Python'] = [7, 8, 8]

first_lecturer = Lecturer('Николай', 'Николаев')
first_lecturer.courses_attached += ['Python']
second_lecturer = Lecturer('Василий', 'Васильев')
second_lecturer.courses_attached += ['Python', 'Git']

reviewer = Reviewer('Александр', 'Александров')

second_student.rate_lecturer(first_lecturer, 'Python', 9)
second_student.rate_lecturer(first_lecturer, 'Python', 9)
second_student.rate_lecturer(second_lecturer, 'Python', 10)
second_student.rate_lecturer(second_lecturer, 'Python', 9)
best_student.rate_lecturer(first_lecturer, 'Python', 10)
best_student.rate_lecturer(first_lecturer, 'Python', 9)
best_student.rate_lecturer(second_lecturer, 'Python', 8)
best_student.rate_lecturer(second_lecturer, 'Python', 9)


print(best_student)
print(second_student)
print(first_lecturer)
print(second_lecturer)

print(second_student.average_grade() < first_lecturer.average_grade())

print(average_grade_all_lecturers([first_lecturer, second_lecturer], 'Python'))
print(average_grade_all_students([best_student, second_student], 'Python'))
# print(best_student.finished_courses)
# print(best_student.courses_in_progress)
# print(best_student.grades)

# cool_mentor = Mentor('Timur', 'Anvartdinov')
# cool_mentor.courses_attached += ['Python']
#
# cool_mentor.rate_hw(best_student, 'Python', 10)
# cool_mentor.rate_hw(best_student, 'Python', 10)
# cool_mentor.rate_hw(best_student, 'Python', 10)

# print(cool_mentor.courses_attached)

# print(best_student.grades)

# lecturer = Lecturer('Николай', 'Николаев')
# lecturer.courses_attached += ['Python']
# reviewer = Reviewer('Александр', 'Александров')
# print(isinstance(lecturer, Mentor)) # True
# print(isinstance(reviewer, Mentor)) # True
# print(lecturer.courses_attached)    # []
# print(reviewer.courses_attached)

# lecturer = Lecturer('Иван', 'Иванов')
# reviewer = Reviewer('Пётр', 'Петров')
# student = Student('Алёхина', 'Ольга', 'Ж')
#
# student.courses_in_progress += ['Python', 'Java']
# lecturer.courses_attached += ['Python', 'C++']
# reviewer.courses_attached += ['Python', 'C++']
#
# print(student.rate_lecturer(lecturer, 'Python', 7))   # None
# print(student.rate_lecturer(lecturer, 'Java', 8))     # Ошибка
# print(student.rate_lecturer(lecturer, 'С++', 8))      # Ошибка
# print(student.rate_lecturer(reviewer, 'Python', 6))   # Ошибка
#
# print(lecturer.grades)  # {'Python': [7]}

