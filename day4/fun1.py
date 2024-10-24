# funkcje - wydzielony fragment kodu, można wywołać wilekrotnie
# funkcja musi byc najpierw zadeklarowana
# w miejscu deklaracji nie uruchammia się funkcja
# zeby funkcję wykonać trzeba ją wywołać

# funkcje niezwracające wyniku
a = 6
b = 8


# deklaracja funkcji
# PEP8 zaleca by funkcja byłą oddzielona dwoma linijami od ciała programu
def dodaj():  # funkcja bezargumentowa
    print(a + b)  # operacja na globalnych zmiennych


def dodaj2(a, b):  # dwa obowiązkowe argumenty a i b
    # zmienne lokalne o tej samej nazwie
    print(a + b)  # pod a i b podstawi wartości przekazane do funkcji


def odejmij(a, b, c=0):  # argument c ma wartość domyślną
    print(a - b - c)


# wywołanie funkcji
# nazwa_funkcji ()
dodaj()  # 14
# dodaj2()  # TypeError: dodaj2() missing 2 required positional arguments: 'a' and 'b'

# przekzanie argumentów po pozycji
dodaj2(56, 89)  # 145, przekazane wartosci
odejmij(89, 6, 7)
odejmij(89, 6)
# 76
# 83

# przekazanie argumentów po nazwie (keywords)
odejmij(b=3, a=9, c=10)
odejmij(b=3, a=9)
# -4
# 6

# mieszany
# pozycyjne przed nazwanymi
odejmij(1, c=9, b=10)  # -18
# odejmij(c=9, 1, 2) # SyntaxError: positional argument follows keyword argument

print(dodaj())
# 14
# None

# TypeError: unsupported operand type(s) for +: 'NoneType' and 'NoneType'
# print(dodaj() + odejmij(7, 9))
