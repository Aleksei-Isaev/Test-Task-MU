"""
Задание №2, вариант №2
Условие:
Написать функцию, которая сортирует список с оценками на основе английской системы.
Всего 5 символов, в порядке убывания: A, B, C, D, F.
Примеры:
sort_grades(['A', 'B', 'C', 'C', 'F', 'A']) -> ['F', 'C', 'C', 'B', 'A', 'A']
sort_grades(['b', 'c', 'C', 'f', 'A']) -> ['F', 'C', 'C', 'B', 'A']
sort_grades([]) -> []
"""


def sort_grades(lst: list):
    print(sorted([i.upper() for i in lst])[::-1])


sort_grades(["A", "B", "C", "C", "F", "A"])
sort_grades(["b", "c", "C", "f", "A"])
sort_grades([])
