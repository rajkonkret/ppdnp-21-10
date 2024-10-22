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
