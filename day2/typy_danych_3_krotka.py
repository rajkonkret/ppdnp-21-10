# krotka (tupla) - kolekcja niemutowalna
# pozwala efektywniej zarządzać pamięcią
# --------------------------------------------
# krotka jednoelementowa - stała - zmienna !!!
# --------------------------------------------

tupla = "Radek"
print(type(tupla))  # <class 'str'>

tupla2 = ("Radek")
print(type(tupla2))  # <class 'str'>

# przecinek jest wyróżnikiem tupli
tupla_3 = "Radek",
print(type(tupla_3))  # <class 'tuple'>

# PEP8 zaleca nawias przy tworzeniu tupli jednoelemntowej
tupla_4 = ("Radek",)
print(type(tupla_4))  # <class 'tuple'>

# tupla_liczba = 43, 55, 22.34, 11, 200
tupla_liczba = (43, 55, 22.34, 11, 200)
print(type(tupla_liczba))  # <class 'tuple'>

print(tupla_4)
print(tupla_liczba)
# przy wypisywaniu nawias będzie (), przy tworzeniu tupli jest opcjonalny
# ('Radek',)
# (43, 55, 22.34, 11, 200)

# tupla jest niemutowalna, nie da się dokonać zmian
# tupla_liczba[2] = 123  # TypeError: 'tuple' object does not support item assignment

del tupla_liczba  # usunięcie całej tupli
# print(tupla_liczba)  # NameError: name 'tupla_liczba' is not defined

tupla_imiona = "Radek", "Tomek", "Olek", "Robert", "Michał", "Anna", "Magda"
print(tupla_imiona)  # ('Radek', 'Tomek', 'Olek', 'Robert', 'Michał', 'Anna', 'Magda')
print(type(tupla_imiona))  # <class 'tuple'>

print(tupla_imiona.count("Radek"))  # występuje jeden raz
print(tupla_imiona.index("Anna"))  # ma index 5

# rozpakowanie tupli (krotki)
tup = 1, 2
print(type(tup))  # <class 'tuple'>
a, b = 1, 2
a, b = tup
print(a, b)  # 1 2
tup_1 = 1, 2, 3
# a, b = tup_1  # ValueError: too many values to unpack (expected 2)
a, *b = tup_1  # * worek na pozostałe dane
print(a, b)  # 1 [2, 3]
print(tupla_imiona)  # ('Radek', 'Tomek', 'Olek', 'Robert', 'Michał', 'Anna', 'Magda')
# name1, name2, name3

name1, *name2, name3 = tupla_imiona
print(name1, name2, name3)  # Radek ['Tomek', 'Olek', 'Robert', 'Michał', 'Anna'] Magda

*name1, name2, name3 = tupla_imiona
print(name1, name2, name3)

name1, name2, *name3 = tupla_imiona
print(name1, name2, name3)
# ['Radek', 'Tomek', 'Olek', 'Robert', 'Michał'] Anna Magda
# Radek Tomek ['Olek', 'Robert', 'Michał', 'Anna', 'Magda']
print(type(name3))  # <class 'list'>
print(name3[2])  # Michał

# sortowanie krotki zwróci nową listę
print(sorted(tupla_imiona))  # ['Anna', 'Magda', 'Michał', 'Olek', 'Radek', 'Robert', 'Tomek']
print(tupla_imiona)  # ('Radek', 'Tomek', 'Olek', 'Robert', 'Michał', 'Anna', 'Magda')

lista = list(tupla_imiona)
print(lista)
print(type(lista))
# ['Radek', 'Tomek', 'Olek', 'Robert', 'Michał', 'Anna', 'Magda']
# <class 'list'>