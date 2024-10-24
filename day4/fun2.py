# funkcje zwracające wynik
# kończą się słówkiem return


# zwraca wynik do miejsca wywołąnia
def dodaj(a, b):
    return a + b


def odejmij(a, b=0, c=0):
    return a - b - c


print(dodaj(6, 9))  # 15
wynik = dodaj(14, 34)
print("Wynik:", wynik)  # Wynik: 48

print(odejmij(1, 2, 3))
print(odejmij(1, 2))
print(odejmij(1, c=10))
# -4
# -1
# -9

print(dodaj(6, 9) + odejmij(7, 9))  # 13
