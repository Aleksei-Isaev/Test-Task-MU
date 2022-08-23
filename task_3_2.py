"""
Задание №3, вариант №2
Условие:
Написать функцию, которая проверяет, являются ли две строки анаграммами?
На вход идут две строки, состоящие из символов английского алфавита.
Примеры:
is_anagram('car', 'tar') -> False
is_anagram('car', 'cart') -> False
is_anagram('anagram', 'nagaram') -> True
is_anagram('beluga', 'begula') -> True
"""


def is_anagram(string_1: str, string_2: str):
    print(sorted(list(string_1)) == sorted(list(string_2)))


is_anagram("car", "tar")
is_anagram("car", "cart")
is_anagram("anagram", "nagaram")
is_anagram("beluga", "begula")
