# funkcja lambda
# skrócony zapis funkcji
# zwraca wynik
# funkcja anonimowa, możliwosc uzycia w miejscu deklaracji
def odejmij(a, b):
    return a - b


print(odejmij(123, 56))  # 67

odejmij2 = lambda a, b: a - b
print(odejmij2(123, 56))  # 67

wiek = lambda x: "dziecko" if x < 10 else ("nastolatek" if x < 18 else "dorosły")
print(wiek(9))  # dziecko
print(wiek(10))  # nastolatek
print(wiek(17))  # nastolatek
print(wiek(18))  # dorosły
print(wiek(25))  # dorosły

# mapowanie danych
lista = [1, 2, 3, 10, 20, 50, 70, 200, 300, 500]

lista_wyn = []
for i in lista:
    lista_wyn.append(i * 2)
print(lista_wyn)  # [2, 4, 6, 20, 40, 100, 140, 400, 600, 1000]

# list comprehension
print([i * 2 for i in lista])  # [2, 4, 6, 20, 40, 100, 140, 400, 600, 1000]


def zmien(x):
    return x * 2


lista_wyn1 = []
for i in lista:
    lista_wyn1.append(zmien(i))

print(lista_wyn1)  # [2, 4, 6, 20, 40, 100, 140, 400, 600, 1000]

# funkcja wyższego rzędu
# map()  - pobiera dane z kolekcji, wykonuje na nich funkcję
print(f"Zastosowanie map(): {list(map(zmien, lista))}")
# Zastosowanie map(): [2, 4, 6, 20, 40, 100, 140, 400, 600, 1000]

# zastosowanie lambdy jako funkcji anonimowej
# uzycie w miejscu deklaracji
# brak przypisanej nazwy
print(f"Zastosowanie map(): {list(map(lambda x: x * 2, lista))}")
# Zastosowanie map(): [2, 4, 6, 20, 40, 100, 140, 400, 600, 1000]
print(f"Zastosowanie map(): {list(map(lambda x: x * 4, lista))}")
print(f"Zastosowanie map(): {list(map(lambda x: x * 12, lista))}")
# Zastosowanie map(): [4, 8, 12, 40, 80, 200, 280, 800, 1200, 2000]
# Zastosowanie map(): [12, 24, 36, 120, 240, 600, 840, 2400, 3600, 6000]

# filtrowanie danych
l3 = []
for i in lista:
    if i < 20:
        l3.append(i)
print(l3)  # [1, 2, 3, 10]

# filter() - zwraca elemnty spełniające warunek zadany funkcją
print(f"Zastosowanie filter() {list(filter(lambda x: x < 20, lista))}")
# Zastosowanie filter() [1, 2, 3, 10]
print(f"Zastosowanie filter() {list(filter(lambda x: x > 20, lista))}")
# Zastosowanie filter() [50, 70, 200, 300, 500]
# x > 5 i x < 150
print(f"Zastosowanie filter() {list(filter(lambda x: x > 5 and x < 150, lista))}")
print(f"Zastosowanie filter() {list(filter(lambda x: 5 < x < 150, lista))}")
# Zastosowanie filter() [10, 20, 50, 70]
# Zastosowanie filter() [10, 20, 50, 70]
