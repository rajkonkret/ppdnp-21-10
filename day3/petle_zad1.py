# pętle - pozwalają nam wykonać dany kod wiele razy
# for - pętla iteracyjna
import random

for i in range(5):  # od 0 do 4
    print(i)
# 0
# 1
# 2
# 3
# 4
for i in range(10):
    pass

for _ in range(5):  # _ niema zmmienna
    print("Test podłoga")
    # print(_)

for i in range(10):
    print(i * 2)

# na podstawie lotto
# przerobic na pętle

lista_kule = list(range(1, 50))
# zapisywac wynik w liscie lista_wyn

lista_wyn = []

for _ in range(6):  # 0 do 5 012345 - 6 obrotów
    wyn = random.choice(lista_kule)
    lista_kule.remove(wyn)
    print(wyn)
    lista_wyn.append(wyn)
# shift tab - cofnięcie wcięcia

print(lista_wyn)  # [4, 10, 28, 6, 26, 14]

for i in range(10):
    if i % 2 == 0:  # modulo, reszta z dzielenia
        print(i, "parzysta")
# 0 parzysta
# 2 parzysta
# 4 parzysta
# 6 parzysta
# 8 parzysta

# list comprehension
lista3 = [j for j in range(10) if j % 2 == 0]
print(lista3)  # [0, 2, 4, 6, 8]

print(lista_wyn)
for c in lista_wyn:  # weż wszystkie elementy kolekcji
    if c > 10:
        print("Większe od 10", c)
    else:
        print("Mniejsze od 10", c)
# [23, 41, 26, 40, 7, 32]
# Większe od 10 23
# Większe od 10 41
# Większe od 10 26
# Większe od 10 40
# Mniejsze od 10 7
# Większe od 10 32

for i in range(0, 10, 2):  # start, stop, krok
    print(i)

# 0
# 2
# 4
# 6
# 8

for i in range(10, 0, -2):  # krok ujemny, krok w tył
    print(i)
# 10
# 8
# 6
# 4
# 2

for i in range(-10, 0):
    print(i)
# -10
# -9
# -8
# -7
# -6
# -5
# -4
# -3
# -2
# -1

# spam += 1    spam = spam + 1
# spam -= 1    spam = spam - 1
# spam *= 1    spam = spam * 1
# spam /= 1    spam = spam / 1
# spam %= 1    spam = spam % 1
for c in lista3:
    if c == 2:
        c += 1  # c = c + 1
        print("tylko dla c=2")
        print(c)
    print("Przy każdym przejsciu pętli")

print("Po zakońćzeniu pętli")
# Przy każdym przejsciu pętli
# tylko dla c=2
# 3
# Przy każdym przejsciu pętli
# Przy każdym przejsciu pętli
# Przy każdym przejsciu pętli
# Przy każdym przejsciu pętli
# Po zakońćzeniu pętli

imiona = ["Radek", 'Tomek', 'Zenek', "Karolina"]
print(imiona)
print(type(imiona))
# ['Radek', 'Tomek', 'Zenek', 'Karolina']
# <class 'list'>

for p in imiona:
    print(p)
# Radek
# Tomek
# Zenek
# Karolina

# wypisac elementy z listy z indeksem
# 0 Radek
# 1 Tomek...
for i in range(len(imiona)):  # range(4) -> 0123
    print(i, imiona[i])
# 0 Radek
# 1 Tomek
# 2 Zenek
# 3 Karolina

for p in imiona:
    print(imiona.index(p), p)
# 0 Radek
# 1 Tomek
# 2 Zenek
# 3 Karolina

# enumerate() - zwraca element kolekcji i numer indeksu
for p in enumerate(imiona):
    print(p)
# (0, 'Radek') -> 0 Radek
# (1, 'Tomek')
# (2, 'Zenek')
# (3, 'Karolina')
a, b = (3, 'Karolina')
print(a, b)  # 3 Karolina

for i, o in enumerate(imiona):
    print(i, o)
# 0 Radek
# 1 Tomek
# 2 Zenek
# 3 Karolina

for i, o in enumerate(imiona, start=1):
    print(i, o)
# 1 Radek
# 2 Tomek
# 3 Zenek
# 4 Karolina

imiona = ["Radek", 'Tomek', 'Zenek', "Karolina"]
wiek = [44, 55, 32, 27]

# wypisac to tak Radek 44
for i in imiona:
    print(i, wiek[imiona.index(i)])
# Radek 44
# Tomek 55
# Zenek 32
# Karolina 27
imiona = ["Radek", 'Tomek', 'Zenek', "Karolina", "Anna"]
wiek = [44, 55, 32, 27]
# for i in imiona:
#     print(i, wiek[imiona.index(i)]) # IndexError: list index out of range

# zip() - łączy kolekcje w jedną, te które mają wszystkie dane
for i in zip(imiona, wiek):
    print(i)
# ('Radek', 44)
# ('Tomek', 55)
# ('Zenek', 32)
# ('Karolina', 27)
for o, w in zip(imiona, wiek):
    print(o, w)
# Radek 44
# Tomek 55
# Zenek 32
# Karolina 27

# 0 Radek 44
for i in enumerate(zip(imiona, wiek)):
    print(i)
# (0, ('Radek', 44))
# (1, ('Tomek', 55))
# (2, ('Zenek', 32))
# (3, ('Karolina', 27))
a, b = (0, ('Radek', 44))
print(a, b)  # 0 ('Radek', 44)
c, d = ('Radek', 44)
print(c, d)  # Radek 44
a, (c, d) = (3, ('Karolina', 27))
print(a, c, d)  # 3 Karolina 27

for i, (o, w) in enumerate(zip(imiona, wiek)):
    print(i, o, w)
# 0 Radek 44
# 1 Tomek 55
# 2 Zenek 32
# 3 Karolina 27
