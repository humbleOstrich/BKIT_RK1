# используется для сортировки
from operator import itemgetter


class Group:
    """Студенческая группа"""
    def __init__(self, id, name, students, course_id):
        self.id = id
        self.name = name
        self.students = students  # количество студентов (количественный признак)
        self.course_id = course_id


class Course:
    """Учебный курс"""
    def __init__(self, id, name):
        self.id = id
        self.name = name


class GroupCourse:
    """
    'Группы курса' для реализации
    связи многие-ко-многим
    """
    def __init__(self, course_id, group_id):
        self.course_id = course_id
        self.group_id = group_id


# Учебные курсы
courses = [
    Course(1, 'Математический анализ'),
    Course(2, 'Программирование на Python'),
    Course(3, 'Базы данных'),
    Course(11, 'Математический анализ (углубленный)'),
    Course(22, 'Программирование на Python (продвинутый)'),
    Course(33, 'Базы данных (практикум)'),
]

# Студенческие группы
groups = [
    Group(1, 'Группа математиков', 25, 1),
    Group(2, 'Группа физиков', 22, 1),
    Group(3, 'Группа программистов', 28, 2),
    Group(4, 'Группа аналитики', 20, 3),
    Group(5, 'Группа экономистов', 24, 3),
    Group(6, 'Группа робототехники', 18, 3),
]

groups_courses = [
    GroupCourse(1, 1),
    GroupCourse(1, 2),
    GroupCourse(2, 3),
    GroupCourse(3, 4),
    GroupCourse(3, 5),
    GroupCourse(3, 6),
    GroupCourse(11, 1),
    GroupCourse(11, 3),
    GroupCourse(22, 3),
    GroupCourse(33, 4),
    GroupCourse(33, 5),
]


def main():
    """Основная функция"""
    # Соединение данных один-ко-многим
    one_to_many = [(g.name, g.students, c.name)
                   for c in courses
                   for g in groups
                   if g.course_id == c.id]

    # Соединение данных многие-ко-многим
    many_to_many_temp = [(c.name, gc.course_id, gc.group_id)
                         for c in courses
                         for gc in groups_courses
                         if c.id == gc.course_id]

    many_to_many = [(g.name, g.students, course_name)
                    for course_name, course_id, group_id in many_to_many_temp
                    for g in groups if g.id == group_id]

    print('Задание Б1')
    # Сортировка по группам
    res_11 = sorted(one_to_many, key=itemgetter(0))
    print(res_11)

    print('\nЗадание Б2')
    res_12_unsorted = []
    # Перебираем все курсы
    for c in courses:
        # Список групп курса
        c_groups = list(filter(lambda i: i[2] == c.name, one_to_many))
        # Если у курса есть группы
        if len(c_groups) > 0:
            res_12_unsorted.append((c.name, len(c_groups)))
    # Сортировка по количеству групп
    res_12 = sorted(res_12_unsorted, key=itemgetter(1), reverse=True)
    print(res_12)

    print('\nЗадание Б3')
    res_13 = {}
    # Перебираем все группы
    for g in groups:
        if g.name.endswith('ов'):
            # Названия курсов группы
            g_courses = [c_name for g_name, _, c_name in many_to_many
                         if g_name == g.name]
            # ключ - группа, значение - список курсов
            res_13[g.name] = g_courses
    print(res_13)


if __name__ == '__main__':
    main()
