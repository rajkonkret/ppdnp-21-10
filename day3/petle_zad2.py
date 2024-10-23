dictionary = {'imie': 'Radek', 'nazwisko': "Kowalski"}
print(type(dictionary))

# wyswietlenie kluczy
for i in dictionary:
    print(i)
# imie
# nazwisko

for i in dictionary.keys():
    print(i)
# imie
# nazwisko

# wyswietlenie wartości
for i in dictionary.values():
    print(i)
# Radek
# Kowalski

# wypisanie par
for i in dictionary.items():
    print(i)
# ('imie', 'Radek')
# ('nazwisko', 'Kowalski')
for k, v in dictionary.items():
    print(k, "=>", v)
# imie => Radek
# nazwisko => Kowalski
#  sep
#         string inserted between values, default a space.
for k, v in dictionary.items():
    print(k, v, sep="=>")
# imie=>Radek
# nazwisko=>Kowalski
print("Tomek", "Radek")  # Tomek Radek, sep=" "
#  end
#         string appended after the last value, default a newline.
for k, v in dictionary.items():
    print(k, v, sep="=>", end="<==>")
# imie=>Radek<==>nazwisko=>Kowalski<==>
print("Tomek")  # ustawiam end="\n" nowa linia
# imie=>Radek<==>nazwisko=>Kowalski<==>Tomek
print()  # ustawiam end="\n" nowa linia

# przerobic na słownik ang_pol
pol_ang = {'kot': 'cat', 'pies': 'dog', 'dach': 'roof'}
ang_pol = {}
for k, v in pol_ang.items():
    ang_pol[v] = k
print(ang_pol)  # {'cat': 'kot', 'dog': 'pies', 'roof': 'dach'}

print({value: key for key, value in pol_ang.items()})
# {'cat': 'kot', 'dog': 'pies', 'roof': 'dach'}
