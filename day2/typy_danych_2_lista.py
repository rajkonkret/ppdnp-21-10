# Kolekcje
# lista - przechowuje wiele elementów, róznego typu na raz
# zachowuje kolejnośc podczas dodawania elementów

# pusta lista
lista = []
print(lista)  # []
print(type(lista))  # <class 'list'>

pusta_lista = list()
print(pusta_lista)
print(type(pusta_lista))
# []
# <class 'list'>


# append() - dodanie elementu do listy (na końcu)
lista.append("Radek")
lista.append("Tomek")
lista.append("Jadwiga")
lista.append("Karolina")
lista.append("Jan")
lista.append("Sylwia")
lista.append("Agata")
lista.append("Mariusz")
print(lista)
# ['Radek', 'Tomek', 'Jadwiga', 'Karolina', 'Jan', 'Sylwia', 'Agata', 'Mariusz']
#     0        1          2         3         4        5         6         7
#    -8       -7          -6       -5         -4       -3        -2        -1
print(lista[0])  # Radek
print(lista[2])  # Jadwiga
print(lista[4])  # Jan

# print(lista[10])# IndexError: list index out of range
# n - 1, len(lista) -1
print(lista[len(lista) - 1])  # Mariusz
print(lista[-1])  # Mariusz, ostatni element
print(lista[-3])  # Sylwia

# wyswietlenie fragmentu listy (slicowanie)
print(lista[0:3])  # ['Radek', 'Tomek', 'Jadwiga'] start:stop -> 012
print(lista[:3])  # ['Radek', 'Tomek', 'Jadwiga']
print(lista[2:])  # ['Jadwiga', 'Karolina', 'Jan', 'Sylwia', 'Agata', 'Mariusz']
print(lista[2:7])  # ['Jadwiga', 'Karolina', 'Jan', 'Sylwia', 'Agata']
# ==
print(lista[:])  # ['Radek', 'Tomek', 'Jadwiga', 'Karolina', 'Jan', 'Sylwia', 'Agata', 'Mariusz']
print(lista[-2:0])  # [] ->[6:0]
print(lista[0:-2])  # ['Radek', 'Tomek', 'Jadwiga', 'Karolina', 'Jan', 'Sylwia'] -> [0:6]
print(lista[2:3])  # ['Jadwiga']
print(lista[2:10])  # ['Jadwiga', 'Karolina', 'Jan', 'Sylwia', 'Agata', 'Mariusz']
print(lista[10:29])  # []
print(lista[2:2])  # []

lista_15 = list(range(15))  # 0 do 14
print(lista_15)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
print(lista_15[0:10:2])  # [start:stop:krok] [0, 2, 4, 6, 8]
print(list(range(0, 15, 2)))  # [0, 2, 4, 6, 8, 10, 12, 14], (start, stop, krok)
print(lista_15[-10])  # 5

# nadpisanie elementu w liście
lista[3] = "Mikołaj"
print(lista)  # ['Radek', 'Tomek', 'Jadwiga', 'Mikołaj', 'Jan', 'Sylwia', 'Agata', 'Mariusz']
print(len(lista))  # 8

# dopisanie
lista.insert(1, "Karolina")
print(lista)  # ['Radek', 'Karolina', 'Tomek', 'Jadwiga', 'Mikołaj', 'Jan', 'Sylwia', 'Agata', 'Mariusz']

# sprawdzenie indeksu dla elemntu, pierwszy napotkany
print(lista.index("Karolina"))  # indeks numer 1

# usunięcie elementu z listy, pierwszy napotkany
lista.append("Mikołaj")  # dodanie jescze raz
print(lista)  # ['Radek', 'Karolina', 'Tomek', 'Jadwiga', 'Mikołaj', 'Jan', 'Sylwia', 'Agata', 'Mariusz', 'Mikołaj']
lista.remove("Mikołaj")
print(lista)  # ['Radek', 'Karolina', 'Tomek', 'Jadwiga', 'Jan', 'Sylwia', 'Agata', 'Mariusz', 'Mikołaj']

# usunięcie po indeksie pop()
print(lista.pop(8))  # Mikołaj
print(lista)  # ['Radek', 'Karolina', 'Tomek', 'Jadwiga', 'Jan', 'Sylwia', 'Agata', 'Mariusz']
print(lista.pop(-2))  # Agata
print(lista.pop())  # usunie ostatni - Mariusz,  Remove and return item at index (default last).

a = 1
b = 3
a = b
print(a, b)  # 3 3
b = 7
print(a, b)  # 3 7

lista_2 = lista  # a = b ? kopia adresu pamięci, referencja
lista_copy = lista.copy()  # kopiowanie elementów listy, dodałem przed clear()
# obie zmienne wskazują na ten sam adres
print(lista_2, lista)
# ['Radek', 'Karolina', 'Tomek', 'Jadwiga', 'Jan', 'Sylwia'] ['Radek', 'Karolina', 'Tomek', 'Jadwiga', 'Jan', 'Sylwia']
lista.clear()  # usunie wszystkie elementy listy
print(lista_2, lista)  # [] []
print(id(lista))
print(id(lista_2))
# 2518043791744
# 2518043791744
print(id(lista_15))
# 2761099645312
# 2761099645312
# 2761103392576
print(lista_copy)
print(id(lista_copy))
# 2914815381888 - lista
# 2914815381888 - lista2
# 2914818817856
# ['Radek', 'Karolina', 'Tomek', 'Jadwiga', 'Jan', 'Sylwia']
# 2914818817792 - lista_copy, lista_copy = lista.copy()

liczby = [54, 999, 34, 22, 12.34, 687]
print(type(liczby))  # <class 'list'>

# zmienia bazową listę
liczby.sort()
print(liczby)  # [12.34, 22, 34, 54, 687, 999]

liczby = [54, 999, 34, 22, 12.34, 687, "A"]
print(type(liczby))  # <class 'list'>

# liczby.sort()  # TypeError: '<' not supported between instances of 'str' and 'int'

print(ord("A"))  # kod ascii dla literki "A", 65

lista_osob = ['radek', 'tomek', 'zenek', 'aldona']
lista_osob.sort()
print(lista_osob)  # ['aldona', 'radek', 'tomek', 'zenek']

lista_osob.sort(reverse=True)
print(lista_osob)  # ['zenek', 'tomek', 'radek', 'aldona']

# kod znaku
print(ord("z"))
print(ord("ł"))
# 122
# 322

lista_osob.reverse()
print(lista_osob)  # ['aldona', 'radek', 'tomek', 'zenek']

liczby[3] = 666
print(liczby[0:3])  # [54, 999, 34]
print(liczby[-2])  # 687
print(liczby)  # [54, 999, 34, 666, 12.34, 687, 'A']

del liczby  # usuniecie listy z pamięci - referencji
# print(liczby)  # NameError: name 'liczby' is not defined

tekst = "Pyth on."
lista1 = list(tekst)
print(lista1)  # ['P', 'y', 't', 'h', ' ', 'o', 'n', '.'] rozpakowanie sekwencji

lista2 = [tekst]
print(lista2)  # ['Pyth on.']

krotka = tuple(lista_osob)  # tuple() - rzutowanie listy na krotke (tuplę)
print(type(krotka))
print(krotka)
# ['aldona', 'radek', 'tomek', 'zenek'] - lista
# <class 'tuple'>
# ('aldona', 'radek', 'tomek', 'zenek') - krotka
