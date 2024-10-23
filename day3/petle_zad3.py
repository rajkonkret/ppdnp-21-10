# while - pętla sterowana warunkiem

# pętla nieskończona
# while True:
#     print("Komunikat 1 !")

licznik = 0
while True:
    licznik += 1
    print("Komunikat 2 !!")
    if licznik > 10:
        break
# Komunikat 2 !!
# Komunikat 2 !!
# Komunikat 2 !!
# Komunikat 2 !!
# Komunikat 2 !!
# Komunikat 2 !!
# Komunikat 2 !!
# Komunikat 2 !!
# Komunikat 2 !!
# Komunikat 2 !!
# Komunikat 2 !!
print(licznik)  # 11

licznik = 0
while licznik < 10:
    licznik += 1
    print("Komunikat 3 !!!")
# Komunikat 3 !!!
# Komunikat 3 !!!
# Komunikat 3 !!!
# Komunikat 3 !!!
# Komunikat 3 !!!
# Komunikat 3 !!!
# Komunikat 3 !!!
# Komunikat 3 !!!
# Komunikat 3 !!!
# Komunikat 3 !!!

password = input("Podaj hasło:")
while password != "secret":
    password = input("Błędne hasło. Podaj ponownie:")
# Błędne hasło. Podaj ponowniesdgsgg
# Błędne hasło. Podaj ponowniefgssgsh
# Błędne hasło. Podaj ponowniefdsg
# Błędne hasło. Podaj ponowniesecret
# Podaj hasło:hfhdhd
# Błędne hasło. Podaj ponownie:secret

lista = []
lista_int = []
#  A string is numeric if all characters in the string are numeric
while True:
    wej = input("Podaj liczbę")  # str
    if not wej.isnumeric():
        break
    lista.append(wej)
    lista_int.append(int(wej))

print(lista)  # ['1', '2', '456', '7890']
print(lista_int)  # ['1', '2', '456', '7890']
# ['5', '7', '56', '12', '24']
# [5, 7, 56, 12, 24]
# Podaj liczbę5
# Podaj liczbę6.78
# ['5']
# [5]

# usunięcie wszystkich wystąpień elementu 5 z listy bez zmiany kolejności
my_list = [1, 5, 2, 3, 5, 4, 5, 6, 5]
while 5 in my_list:
    my_list.remove(5)

print(my_list)  # [1, 2, 3, 4, 6]
