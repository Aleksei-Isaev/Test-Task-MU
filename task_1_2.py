"""
Задание №1, вариант №2
Условие:
Написать функцию, которая находит самые повторяющиеся слова в строке.
Пример:
simple_text('Am I want write code? Yeah! I like it') → I
simple_text('Hi! How are you? Hi! I am okay') → Hi
simple_text('test text test and test that again') → test
"""

import string
from collections import Counter


def simple_text(s: str):
    result_list = []
    for i in s.split():
        result_list.append(
            i.translate(str.maketrans("", "", string.punctuation))
        )

    print(Counter(result_list).most_common(1))


simple_text("Am I want write code? Yeah! I like it")
simple_text("Hi! How are you? Hi! I am okay")
simple_text("test text test and test that again")
