# słownik - para klucz-wartość
# {'user': 'Radek', 'wiek': 78}
# słownik jest odpowiednikiem jsona w pythonie
# '{"name":"John", "age":30, "car":null}'
# klucze nie mogą się powtórzyć


# pusty słownik
dictionary = dict()
print(type(dictionary))  # <class 'dict'>
print(dictionary)  # {}

dictionary_1 = {}
print(type(dictionary_1))
print(dictionary_1)
# <class 'dict'>
# {}

# dodawanie elementów do słownika
dictionary['imie'] = "Radek"
print(dictionary)  # {'imie': 'Radek'}
dictionary['wiek'] = 38
print(dictionary)  # {'imie': 'Radek', 'wiek': 38}

print(dictionary.keys())  # dict_keys(['imie', 'wiek'])
print(dictionary.values())  # dict_values(['Radek', 38])
print(dictionary.items())  # dict_items([('imie', 'Radek'), ('wiek', 38)])

# nadpisanie elementu
dictionary['imie'] = "Tomek"
print(dictionary)  # {'imie': 'Tomek', 'wiek': 38}

# wypisanie elementu - wartości dla klucza
print(dictionary['imie'])  # Tomek
# print(dictionary['Imie'])  # KeyError: 'Imie', KeyError	Raised when a key does not exist in a dictionary
print(dictionary.get('Imie'))  # None
print(dictionary.get('Imie', "Domyślna"))  # Domyślna

dictionary.update({'date': '12-12-2024'})
print(dictionary)  # {'imie': 'Tomek', 'wiek': 38, 'date': '12-12-2024'}

dict_small = {'x': 2}
dict_small.update([('y', 3), ('z', 4)])
print(dict_small)  # {'x': 2, 'y': 3, 'z': 4}

dict_small.update([("k", 8)])  # lista krotek z jedym elementem
print(dict_small)  # {'x': 2, 'y': 3, 'z': 4, 'k': 8}

# # input()  - pobiera dane od uzytkownika
# tekst = input("Podaj imię")
# print("Masz na imię", tekst)
# Podaj imięTomek
# Masz na imię Tomek

# aplikacja kalkulator
# pobrac dwie liczby -> input x 2
# wyswietlic wynik (dodawanie) -> print
# input zwraca str
# a = int(input("Podaj pierwszą liczbę"))
# b = input("Podaj drugą liczbę")
# print(a + float(b))
# Podaj pierwszą liczbę3
# Podaj drugą liczbę4
# 7.0

# napisać aplikacji słownik
# pol - ang
# słowa do przetłumaczenia -> klucze
# pobrac słowo do przetłummaczenia
# wyswietlic tłumaczenie -> wartość dla klucza
# słownik z danymi
#  print wyswietli klucze
# input pobierze słówko od użytkownika
# print wyświetli tłumaczenie
pol_ang = {'kot': 'cat', 'pies': 'dog', 'dach': 'roof'}
print("Znam takie słówka", pol_ang.keys())
odp = input("Podaj słówko do przetłumaczenia")
# print(pol_ang[odp.strip().casefold()])
print(pol_ang.get(odp.strip().casefold(), "nie mo"))