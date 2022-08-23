"""
Задание №4, вариант №1
Условие:
Написать функцию, которая сортирует список, но все четные числа должны остаться на своем месте.
Примеры:
sort_array([3, 1]) -> [1, 3]
sort_array([3, 2, -1, 4]) -> [-1, 2, 3, 4]
sort_array([5, 3, 2, 8, 1, 4]) -> [1, 3, 2, 8, 5, 4]
"""


def sort_array(array: list):
    odd_values = []
    odd_indices = []

    for i in range(len(array)):
        if array[i] % 2 != 0:
            odd_values.append(array[i])
            odd_indices.append(i)

    odd_values.sort()

    for i in range(len(odd_values)):
        array[odd_indices[i]] = odd_values[i]

    print(array)


sort_array([3, 1])
sort_array([3, 2, -1, 4])
sort_array([5, 3, 2, 8, 1, 4])
