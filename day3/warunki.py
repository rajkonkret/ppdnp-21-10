# instrukcje warunkowe
# instrukcje sterowania przepływem prograamu
# warunek musi zwracac bool
# if
from day2.typy_danych_2_lista import lista

odp = True
print(bool(odp))  # True
odp = False
if odp:  # odp == True
    # blok wykonywany po if, gdy warunek spełniony
    # wcięcie 4 spacje
    print("Brawo")
    print("Brawo")
    print("Brawo")
    print("Brawo")
    # print("Brawo")unexpected indent

print("kolejna instrukcja")
# True
# Brawo
# Brawo
# Brawo
# Brawo
# kolejna instrukcja

odp = "Radek"
print(bool(odp))  # True
if odp:  # czy cokolwiek jest w zmiennej
    print("Radek")  # Radek

if odp == "Radek":  # == - porównanie
    print("To jest nadal Radek")  # To jest nadal Radek

if odp == "Tomek":
    print("To jest Tomek")
else:  # w przeciwnym wypadku
    print("To nie jest Tomek")  # To nie jest Tomek

# Indent Rainbow - plugin do pokazywania wcięć

# podatek = 0
# zarobki = int(input("Podaj zarobki"))
# if zarobki < 10_000:  # do 9999
#     podatek = 0
# elif zarobki < 30000:
#     podatek = 0.2
# elif zarobki < 100_000:
#     podatek = 0.4
# else:
#     podatek = 0.9
#
# # jeden warunek spełniony wychodzimy z drzewa warunków
# print(f"Podatek wynosi {podatek * zarobki}")
# # dodac dla zarobków od 10000 do 29999 podatek 0.2
# # zarobki > 9999 and  zarobki < 30000 -> 10000 < zarobki < 30000

suma_zam = 150
if suma_zam > 100:
    rabacik = 25
else:
    rabacik = 0
print(f"Rabat wynosi", rabacik)  # Rabat wynosi 25

rabat = 25 if suma_zam > 100 else 0
print(f"Rabat wynosi", rabat)  # Rabat wynosi 25 ternary operator, operator warunkowy

# zasymulujemy system zbierania logów
# zmienne będą przechowywac nazwę systemu jaki przysłał log
# email, console, inny (else)
# console: "Stało się coś strasznego"
# email "System email"
# inny: "Nie znam takiego systemu"
