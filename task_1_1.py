"""
Задание №1, вариант №1
Условие:
Написать функцию, которая находит самые повторяющиеся слова в строке.
Пример:
simple_text('Am I want write code? Yeah! I like it') → I
simple_text('Hi! How are you? Hi! I am okay') → Hi
simple_text('test text test and test that again') → test
"""

import string


def simple_text(s: str):
    s = s.split()
    target_set = set(s)

    most_frequent = None
    quantity_most_frequent = 0

    for item in target_set:
        quantity = s.count(item)

        if quantity > quantity_most_frequent:
            quantity_most_frequent = quantity
            most_frequent = item

    print(most_frequent.translate(str.maketrans("", "", string.punctuation)))


simple_text("Am I want write code? Yeah! I like it")
simple_text("Hi! How are you? Hi! I am okay")
simple_text("test text test and test that again")
