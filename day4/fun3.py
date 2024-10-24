# zmienne globalne
a = 10
b = 10


def dodaj():
    a = 7  # zmienne lokalne
    b = 8
    print(a + b)


def dodaj2():
    print(a + b)


def dodaj3():
    global a
    a = 9  # a globalne, nadpisze wartość globalną!
    b = 89
    print(a + b)


print(f"Wartość a z góry (globalna) {a=}")  # Wartość a z góry (globalna) a=10
dodaj()  # 15
print(f"Wartość a z góry (globalna) {a=}")  # Wartość a z góry (globalna) a=10
dodaj2()  # 20
print(f"Wartość a z góry (globalna) {a=}")  # Wartość a z góry (globalna) a=10
dodaj3()  # 98
print(f"Wartość a z góry (globalna) {a=}")  # Wartość a z góry (globalna) a=9
dodaj2()  # 19
