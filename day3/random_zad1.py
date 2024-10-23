import random

# do działań na liczbach pseudolosowych

print(random.randint(1, 100))  # 66, int od 1 do 100
print(random.randrange(1, 100))  # int, od 1 do 99
print(random.randrange(5))  # int od 0 do 4
print(random.random())  # float, 0.6442783396789321 od 0 do 0.9999999
print(random.random() * 10)  # float,3.476204299776715 od 0 do 9.9999999

lista = [67, 45, 32, 68, 89, 90, 42]
print(random.choice(lista))  # 68

lista_kule = list(range(1, 50))
print(lista_kule)

print(random.choice(lista_kule))
wyn = random.choice(lista_kule)
lista_kule.remove(wyn)
print(wyn)

print(random.choices(lista_kule, k=6))  # powtarzające się
print(random.sample(lista_kule, k=6))  # [27, 32, 31, 9, 30, 11], bez powtórzeń
print(random.sample(lista_kule, 6))  # [27, 32, 31, 9, 30, 11], bez powtórzeń
# [33, 14, 46, 1, 23, 37]
# [8, 37, 15, 11, 7, 27]
