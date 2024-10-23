# wyjątki - błedy programu
# print(5 / 0)
# Traceback (most recent call last):
#   File "C:\Users\CSComarch\PycharmProjects\ppdnp-21-10\day3\wyjatki.py", line 2, in <module>
#     print(5 / 0)
#           ~~^~~
# ZeroDivisionError: division by zero

# przechwytywanie i obsługa wyjątków  (błędów)
try:
    # print(5 / 0)
    # print(3 / "0")
    # print(5 / int("A"))
    wynik = 90 / z # Bład name 'z' is not defined
    # wynik = 90 / 3
except ZeroDivisionError:
    print("Nie dziel przez zero")
except TypeError:
    print("Bład typu")
except ValueError:
    print("Bład wartości")
except Exception as e:  # pozostałe błedy
    print("Bład", e)
else:  # tylko gdy nie ma błedu
    print("Wynik", wynik)
finally:  # wykona się zawsze
    print("Obliczenia dla następnego wiersza")

print("Program działa nadal")
# Nie dziel przez zero
# Program działa nadal
# Wynik 30.0
# Program działa nadal
# Wynik 30.0
# kolejne obliczenia
# Program działa nadal

# Nie dziel przez zero
# kolejne obliczenia
# Program działa nadal

# Bład name 'z' is not defined
# Obliczenia dla następnego wiersza
# Program działa nadal

# try - except [else - finally]
