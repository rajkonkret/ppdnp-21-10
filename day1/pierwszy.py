import sys

print()  # wypisz/wydrukuj
# Process finished with exit code 0 - brak błędu
# PEP8
# ctrl alt l - formatowanie kodu

print("Nazywam się Radek")
print('Nazywam się Radek')
print('Nazywam się Radek')
print('Nazywam się Radek')
print('Nazywam się Radek')
# ctrl d - powielanie lisni z kursorem
#
# Nazywam się Radek
# Nazywam się Radek
# Nazywam się Radek
# Nazywam się Radek
# Nazywam się Radek
# ctrl / - komentowanie zaznaczonego bloku kodu

# print('NAzywam się Radek")
#   File "C:\Users\CSComarch\PycharmProjects\ppdnp-21-10\day1\pierwszy.py", line 20
#     print('NAzywam się Radek")
#           ^
# SyntaxError: unterminated string literal (detected at line 20)

# dane typu tekstowego - str - string
# type() - sprawdzenie typu danych
print(type("Radek"))  # <class 'str'>
print("39")  # 39
print(type("39"))  # <class 'str'>

print(39)
print(type(39))  # <class 'int'> - liczby całkowite
# print("39" + 39)  # TypeError: can only concatenate str (not "int") to str
print("39" + '39')  # 3939
print(39 + 39)  # 78

print(5 * "39")  # 3939393939
print(sys.int_info)
# sys.int_info(bits_per_digit=30
# , sizeof_digit=4,
# default_max_str_digits=4300,
# str_digits_check_threshold=640)

# print("39" + 39)  # TypeError: can only concatenate str (not "int") to str

print(int("39") + 39)  # int() - rzutoanie, zamiana na liczbę całkowitą, 78
print("39" + str(39))  # 3939, łaczenie tekstów, konkatenacja str() - rutowanie na str

# print(int("A"))  # ValueError: invalid literal for int() with base 10: 'A'

print("8" + "8" + "8")
print(8 + 8 + 8)  # 24

