"""
Задание №5, вариант №1
Условие:
Написать функцию которая, будет переводить римские символы в привычную нам десятичную систему.
Пример:
roman_to_int('XXI') -> 21
roman_to_int('IV') -> 4
roman_to_int('I') -> 1
"""


def roman_to_int(roman_number: str):
    roman_decoding = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    result = 0

    for i in range(len(roman_number)):

        if i != 0 and roman_decoding[roman_number[i - 1]] < roman_decoding[roman_number[i]]:
            result = result + roman_decoding[roman_number[i]] - roman_decoding[roman_number[i - 1]] * 2
        else:
            result = result + roman_decoding[roman_number[i]]

    print(result)


roman_to_int("XXI")
roman_to_int("IV")
roman_to_int("I")
