"""
Задание №3, вариант №1
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
    array = [0 for _ in range(26)]

    for i in string_1:
        array[ord(i) - ord("a")] += 1
    for i in string_2:
        array[ord(i) - ord("a")] -= 1
        
    print(max(array) == 0 and min(array) == 0)


is_anagram("car", "tar")
is_anagram("car", "cart")
is_anagram("anagram", "nagaram")
is_anagram("beluga", "begula")
