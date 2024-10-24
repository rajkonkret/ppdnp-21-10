# klasa - elemnt programowania obiektowego
# klasa - szablon, przepis
# wskazuje cechy i funkcje
# cechy = zmienne
# funkcje
# paradygmaty programowania obiektowego
# hemetyzacja, dziedziczenie, polimorfizm, abstrakcja
# definicja klasy nie uruchamima klasy
# budowanie obiektu klasy uruchmia metody w klasie
# obiekt (instancja)


# definicja klasy
# PEP8 - nazwy klas z duzej litery
class Human:
    """
    Klasa Human opisująca człowieka w pythonie
    """

    imie = ""
    wiek = None
    plec = "k"


# tworzenie obiektu klasy
cz1 = Human()
print(Human.__doc__)  # Klasa Human opisująca człowieka w pythonie
print(print.__doc__)
# Prints the values to a stream, or to sys.stdout by default.
#
#   sep
#     string inserted between values, default a space.
#   end
#     string appended after the last value, default a newline.
#   file
#     a file-like object (stream); defaults to the current sys.stdout.
#   flush
#     whether to forcibly flush the stream.
# cd .\day4
# pydoc - b - serwer z dokumentacją
# pydoc -w kl1 - generowanie pliku html z dokumentacją
print(cz1.wiek)
print(cz1.imie)
print(cz1.plec)
# None
#
# k
cz1.wiek = 56
cz1.imie = "Tomek"
cz1.plec = "m"
print(cz1.wiek)
print(cz1.imie)
print(cz1.plec)
# 56
# Tomek
# m
