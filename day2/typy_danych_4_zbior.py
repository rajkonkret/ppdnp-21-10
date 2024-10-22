# zbiór (set) - przechowuje unikalne wartości
# nie zachowuje kolejności przy dodawaniu elementów
# nie posiada indeksu

lista = [44, 55, 66, 777, 33, 22, 11, 33, 11]
zbior = set(lista)
print(zbior)
print(type(zbior))
# {33, 66, 777, 11, 44, 22, 55} straciliśmy kolejność
# <class 'set'>

# utworzenie pustego zbioru
zb2 = set()
print(zb2)  # set()
print(type(zb2))  # <class 'set'>

# dodanie lementu do zbioru add()
zbior.add(33)
zbior.add(33)
zbior.add(18)
zbior.add(18)
zbior.add(18)
zbior.add(24)
print(zbior)
# <class 'set'>
# {33, 66, 777, 11, 44, 18, 22, 55, 24}

# usunięcie elementu ze zbioru
zbior.remove(55)
print(zbior)  # {33, 66, 777, 11, 44, 18, 22, 24}

# pop() - usunięcie pierwszego elementu
print(zbior.pop())  # 33
print(zbior)  # {66, 777, 11, 44, 18, 22, 24}
zmienna = zbior.pop()
print(zmienna)  # 66

zbior_copy = zbior.copy()
print(zbior_copy)
print(id(zbior))
print(id(zbior_copy))
# {18, 22, 24, 777, 11, 44}
# 2496708288672
# 2496708284192
