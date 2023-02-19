# Класс студенты:
class Students:
    def __init__(self, name, surname):
        pass
        self.name = name
        self.surname = surname
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    # Студент оценивает лектора:
    def get_grades(self, _lector, course, grades):
        if isinstance(_lector, Lecturers) and \
                course in self.courses_in_progress and course in _lector.courses_attached:
            if course in _lector.grades:
                _lector.grades[course] += [grades]
            else:
                _lector.grades[course] = [grades]
        else:
            print('Ошибка.')

    # Метод расчета среднего балла студента:
    def __gpa(self):
        # В список marks мы будем собирать средние баллы по каждому направлению обучения студента:
        marks = []
        for values in self.grades.values():
            marks += [round(sum(values) / len(values), 1)]
        # gpa - общий средний балл по всем направлениям обучения студента.
        gpa = round(sum(marks) / len(marks), 1)
        return gpa

    # Перегрузка магического метода __str__ для класса Students.
    def __str__(self):
        return f"Имя: {self.name}\n" \
               f"Фамилия: {self.surname} \n" \
               f"Средняя оценка за домашние задания: {self.__gpa()}\n" \
               f"Курсы в процессе изучения: {', '.join(self.courses_in_progress)}\n" \
               f"Завершенные курсы: {', '.join(self.finished_courses)}"

    # Реализуем возможность сравнения студентов по среднему баллу:
    def __lt__(self, other):
        if not isinstance(other, Students):
            print(f'{other} не студент)')
        else:
            return self.__gpa() < other.__gpa()


# Класс преподаватели:
class Mentors:

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


# Подкласс лекторы:
class Lecturers(Mentors):

    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    # Метод расчета среднего балла лектора:
    def __gpa(self):
        # В список marks мы будем собирать средние баллы по каждому направлению работы лектора:
        marks = []
        for values in self.grades.values():
            marks += [round(sum(values) / len(values), 1)]
        # gpa - общий средний балл по всем направлениям работы лектора.
        gpa = round(sum(marks) / len(marks), 1)
        return gpa

    # Перегрузка магического метода __str__ для класса Lecturers.
    def __str__(self):
        return f"Имя: {self.name}\n" \
               f"Фамилия: {self.surname} \n" \
               f"Средняя оценка за лекции: {self.__gpa()}"

    # Реализуем возможность сравнения лекторов по среднему баллу:
    def __lt__(self, other):
        if not isinstance(other, Lecturers):
            print(f'{other} не лектор)')
        else:
            return self.__gpa() < other.__gpa()


# Подкласс эксперты:
class Reviewers(Mentors):

    # Эксперты оценивают студентов:
    def get_grades(self, _student, course, grades):
        if isinstance(_student, Students) and \
                course in self.courses_attached and course in _student.courses_in_progress:
            if course in _student.grades:
                _student.grades[course] += [grades]
            else:
                _student.grades[course] = [grades]
        else:
            print('Ошибка.')

    # Перегрузка магического метода __str__ для класса Reviewers.
    def __str__(self):
        return f"Имя: {self.name}\n" \
               f"Фамилия: {self.surname}"


# Подсчет средней оценки за домашние задания по всем студентам в рамках конкретного курса:
def gpa_student(students, course):
    marks = {course: []}
    for _student in students:
        if course in _student.courses_in_progress:
            marks[course] += _student.grades[course]
    return print(
        f'Средний балл по ДЗ всех студентов курса {course}: ' \
        f'{round(sum(marks[course]) / len(marks[course]), 1)}'
    )


# Подсчет средней оценки за лекции всех лекторов в рамках курса:
def gpa_lector(lectors, course):
    marks = {course: []}
    for _lector in lectors:
        if course in _lector.courses_attached:
            marks[course] += _lector.grades[course]
    return print(
        f'Средняя оценка всех лекторов курса {course}: ' \
        f'{round(sum(marks[course]) / len(marks[course]), 1)}'
    )


# Студент №1:
student = Students('Студент', 'Студентов')

# Назначаем Студенту №1 курсы для изучения:
student.courses_in_progress.append('Python')
student.courses_in_progress += ['NodeJS']

# Указываем курсы, которые уже окончил Студенту №1:
student.finished_courses += ['Введение в программирование', 'JavaScript']
# print(student.__dict__)

# Студент №2:
student_W = Students('Студентка', 'Студентова')

# Назначаем Студенту №2 курсы для изучения:
student_W.courses_in_progress.append('Python')
student_W.courses_in_progress += ['Ruby']

# Указываем курсы, которые уже окончил Студенту №2:
student_W.finished_courses += ['Основы MySQL', 'PHP']
# print(student_W.__dict__)

# Эксперт №1:
reviewer = Reviewers('Эксперт', 'Экспертов')

# Эксперт №1 работает на курсах:
reviewer.courses_attached += ['Python', 'NodeJS', 'Ruby']
# print(reviewer.__dict__)

# Эксперт №2:
reviewer_W = Reviewers('Экспертка', 'Экспертова')

# Эксперт №2 работает на курсах:
reviewer_W.courses_attached += ['Python']
# print(reviewer_W.__dict__)

# Лектор N1:
lector = Lecturers('Лектор', 'Лекторов')

# Лектор №1 работает на курсах:
lector.courses_attached += ['Python', 'NodeJS']
# print(lector.__dict__)

# Лектор N2:
lector_W = Lecturers('Лекторша', 'Лекторова')

# Лектор №2 работает на курсах:
lector_W.courses_attached += ['Python', 'Ruby']
# print(lector_W.__dict__)

# Эксперты выставляют оценки Студенту №1:
reviewer.get_grades(student, 'Python', 1)
reviewer_W.get_grades(student, 'Python', 1)
reviewer.get_grades(student, 'NodeJS', 2)
# print(student.name, student.surname, student.grades)

# Эксперты выставляют оценки Студенту №2:
reviewer.get_grades(student_W, 'Python', 3)
reviewer_W.get_grades(student_W, 'Python', 3)
reviewer.get_grades(student_W, 'Ruby', 4)
# print(student_W.name, student_W.surname, student_W.grades)

# Студенты №1 и №2 выставляют оценки Лектору №1:
student.get_grades(lector, 'Python', 5)
student_W.get_grades(lector, 'Python', 5)
student.get_grades(lector, 'NodeJS', 6)
# print(lector.name, lector.surname, lector.grades)

# Студенты №1 и №2 выставляют оценки Лектору №2:
student_W.get_grades(lector_W, 'Ruby', 7)
student.get_grades(lector_W, 'Python', 8)
student_W.get_grades(lector_W, 'Python', 8)
# print(lector_W.name, lector_W.surname, lector_W.grades)

# Вывод результата на экран:
print('------------------------- Эксперт №1 -----------------------------')
print(reviewer)
print('------------------------- Эксперт №2 -----------------------------')
print(reviewer_W)
print('-------------------------- Лектор №1 -----------------------------')
print(lector)
print('-------------------------- Лектор №2 -----------------------------')
print(lector_W)
print('-------------------------- Студент №1 ----------------------------')
print(student)
print('-------------------------- Студент №2 ----------------------------')
print(student_W)
print('--------------------- Сравнение студентов ------------------------')
print(student > student_W)
print('--------------------- Сравнение лекторов -------------------------')
print(lector > lector_W)
print('---- Средний балл по всем ДЗ всех студентов указанного курса -----')
print()
gpa_student([student, student_W], 'Python')
gpa_student([student, student_W], 'NodeJS')
gpa_student([student, student_W], 'Ruby')
print()
print('----- Средняя оценка за лекции всех лекторов в рамках курса ------')
print()
gpa_lector([lector, lector_W], 'Python')
gpa_lector([lector, lector_W], 'NodeJS')
gpa_lector([lector, lector_W], 'Ruby')
