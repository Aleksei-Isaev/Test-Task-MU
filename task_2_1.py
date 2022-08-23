"""
Задание №2, вариант №1
Условие:
Написать функцию, которая сортирует список с оценками на основе английской системы.
Всего 5 символов, в порядке убывания: A, B, C, D, F.
Примеры:
sort_grades(['A', 'B', 'C', 'C', 'F', 'A']) -> ['F', 'C', 'C', 'B', 'A', 'A']
sort_grades(['b', 'c', 'C', 'f', 'A']) -> ['F', 'C', 'C', 'B', 'A']
sort_grades([]) -> []
"""


def sort_grades(lst: list):
    result_list = []

    for letter in lst:
        if letter == letter.lower():
            result_list.append(letter.upper())
        else:
            result_list.append(letter)

    result_list = sorted(result_list)

    print(result_list[::-1])


sort_grades(["A", "B", "C", "C", "F", "A"])
sort_grades(["b", "c", "C", "f", "A"])
sort_grades([])
