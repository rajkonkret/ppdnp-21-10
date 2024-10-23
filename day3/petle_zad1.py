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
