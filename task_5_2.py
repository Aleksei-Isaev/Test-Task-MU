"""
Задание №5, вариант №2
Условие:
Написать функцию которая, будет переводить римские символы в привычную нам десятичную систему.
Пример:
roman_to_int('XXI') -> 21
roman_to_int('IV') -> 4
roman_to_int('I') -> 1
"""


def roman_to_int(roman_number: str):
    roman_decoding = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

    roman_number = \
        roman_number.replace(
            "IV", "IIII"
        ).replace(
            "IX", "VIIII"
        ).replace(
            "XL", "XXXX"
        ).replace(
            "XC", "LXXXX"
        ).replace(
            "CD", "CCCC"
        ).replace(
            "CM", "DCCCC"
        )

    print(sum(map(lambda x: roman_decoding[x], roman_number)))


roman_to_int("XXI")
roman_to_int("IV")
roman_to_int("I")
