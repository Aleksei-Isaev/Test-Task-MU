"""
Задание №4, вариант №2
Условие:
Написать функцию, которая сортирует список, но все четные числа должны остаться на своем месте.
Примеры:
sort_array([3, 1]) -> [1, 3]
sort_array([3, 2, -1, 4]) -> [-1, 2, 3, 4]
sort_array([5, 3, 2, 8, 1, 4]) -> [1, 3, 2, 8, 5, 4]
"""


def sort_array(array: list):
    odd_numbers = iter(sorted(filter(lambda x: x % 2, array)))
    print([next(odd_numbers) if i % 2 else i for i in array])


sort_array([3, 1])
sort_array([3, 2, -1, 4])
sort_array([5, 3, 2, 8, 1, 4])
