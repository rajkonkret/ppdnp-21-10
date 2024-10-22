import sys

wiek = 47
rok = 2024
# ctrl alt l
temp = 36.6

print(temp)
print(type(temp))  # <class 'float'>, zmiennoprzecinkowe

print(wiek + rok)  # 2071
print(wiek - rok)  # -1977
print(wiek * rok)  # 95128
print(wiek / rok)  # 0.023221343873517788

print(rok // wiek)  # 43, część całkowita z dzielenia
print(rok % wiek)  # 3, modulo, reszta z dzielenia
print(5 % 2)  # 1 bo 2 * 2 + 1 = 5

print(wiek ** rok)  # potęgowanie
# len() - długość
print(len(str(wiek ** rok)))  # długość 3385 znaków
# print(len(str(wiek ** rok ** 2)))
# ValueError: Exceeds the limit (4300 digits) for integer string conversion; use sys.set_int_max_str_digits() to increase the limit

print(54 - 5 * 43 + 4 / 2 + 4 / 2)  # -157.0
print(54 - 5 * 43 + (4 / 2 + 4) / 2)  # -158.0

# przy liczbach występują bład zaokrąglenia
print(0.2 + 0.8)  # 1.0
print(0.2 + 0.7)  # 0.8999999999999999
# the sum 12.345 + 1.0001 = 13.3451 might be rounded to 13.345
print(sys.float_info)
# sys.float_info(max=1.7976931348623157e+308,
#                max_exp=1024,
#                max_10_exp=308,
#                min=2.2250738585072014e-308,
#                min_exp=-1021,
#                min_10_exp=-307,
#                dig=15,
#                mant_dig=53,
#                epsilon=2.220446049250313e-16, radix=2, rounds=1)

# decimal - typ danych do ominięcia błedu zaokrąglenia

print(f"Sprawdzenie zmiennej {temp} {wiek}")  # Sprawdzenie zmiennej 36.6 47
print(f"""
{wiek}
    {temp}""")
# "
# 47
#     36.6"

# typ logiczny
# prawda fałsz
# 1 - prawde, 0 - fałsz
# True False - obowiązkowo z dużej litery

czy_znasz_pythona = True
print(czy_znasz_pythona)  # True
print(type(czy_znasz_pythona))  # <class 'bool'>, typ boolean, typ logiczny

print(int(True))  # int() - rzutowanie na liczbę, 1
print(int(False))  # 0

print(bool(1))  # bool() - rzutowanie na logiczny
print(bool(0))  # False

print(bool(100))  # True
print(bool(-10))  # True
print(bool("radek"))  # True

print(bool(0))  # False
print(bool(""))  # False
print(bool(None))  # None - nic, odpowiednik null

# and - i
# Expression    Evaluates to
# True and True    True
# True and False    False
# False and True    False
# False and False    False
# The or Operator’s Truth Table:
#

# or - lub
# Expression    Evaluates to
# True or True    True
# True or False    True
# False or True    True
# False or False    False
# The not Operator’s Truth Table:
#

# not - negacja
# Expression    Evaluates to
# not True    False
# not False

print(True and True)  # True
print(True and False)  # False

a = 8
b = 6

# wynik porównań jest typu bool
print(f"Porównanie {a} > {b} = {a > b}")  # Porównanie 8 > 6 = True
print(f"Porównanie {a} < {b} = {a < b}")  # Porównanie 8 < 6 = False

print(f"Porównanie {a <= b= }")  # Porównanie a <= b= False
print(f"Porównanie {a >= b= }")  # Porównanie a >= b= True

print(f"Porównanie {a} == {b} = {a == b}")  # przyrównanie, Porównanie 8 == 6 = False
print(f"Porównanie {a} != {b} = {a != b}")  # czy rózżne?, Porównanie 8 != 6 = True
# ctrl d - powielanie
# shift alt strzałka - przenoszenie linijki
print(f"Porównanie {a} > {b} = {a > b}")  # Porównanie 8 > 6 = True
