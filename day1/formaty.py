user = "Tomek"  # str
wiek = 39  # int
wersja = 3.900001  # zmiennoprzecinkowe, float
print(type(wersja))  # <class 'float'>

liczba = 456789123690  # int

# sprawdza typy
print("Witaj %s, masz teraz %d lat." % (user, wiek))  # Witaj Tomek, masz teraz 39 lat.
# print("Witaj %d, masz teraz %s lat." % (user, wiek))  # TypeError: %d format: a real number is required, not str
# %s - string
# %d - digit - liczba

print("Witaj %(user)s, masz teraz %(wiek)d lat." % {'user': user, "wiek": wiek})
# Witaj Tomek, masz teraz 39 lat.
print("Czesc %(user)s, ciesze się, że Cię widzę %(user)s" % {'user': user})
# Czesc Tomek, ciesze się, że Cię widzę Tomek

print("witaj {}, masz teraz {} lat.".format(user, wiek))  # witaj Tomek, masz teraz 39 lat.

print(f"Witaj {user}, masz teraz {wiek} lat.")  # Witaj Tomek, masz teraz 39 lat.
print("Witaj", user)  # Witaj Tomek
# f - string, tekst sformatowany

print("Uzywamy wersji Pythona %i" % 3)  # Uzywamy wersji Pythona 3
print("Uzywamy wersji Pythona %f" % 3)  # Uzywamy wersji Pythona 3.000000
print("Uzywamy wersji Pythona %.2f" % 3.9)  # Uzywamy wersji Pythona 3.90
print("Uzywamy wersji Pythona %.1f" % 3.9)  # Uzywamy wersji Pythona 3.9
print("Uzywamy wersji Pythona %.0f" % 3.9)  # Uzywamy wersji Pythona 4, zaokraągli
print("Uzywamy wersji Pythona %.f" % 3.9)  # Uzywamy wersji Pythona 4, zaokraągli
# zaokrągle przy ywświetlaniu
x = 3.14
print("Zero miejsc po przecinku %.f" % x)
print("X nie zmienia się", x)
# Zero miejsc po przecinku 3
# X nie zmienia się 3.14

y = round(x)
print("y=", y)
print(f"{x=}")
# y= 3
# x=3.14

x = 3.1415
print(round(x, 2))  # 3.14

print(f"Uzywamy wersji python {wersja}")
print(f"Uzywamy wersji python {wersja:.1f}")
print(f"Uzywamy wersji python {wersja:.2f}")
print(f"Uzywamy wersji python {wersja:.0f}")
# print(f"Uzywamy wersji python {wersja:.f}")  # ValueError: Format specifier missing precision
# Uzywamy wersji python 3.900001
# Uzywamy wersji python 3.9
# Uzywamy wersji python 3.90
# Uzywamy wersji python 4

print(f"{user:>10}")  # "     Tomek", wyrównanie do prawej
print(f"{user:<20}")  # "Tomek          ", wyrównanie do lewej
print(f"{user:^30}")  # "            Tomek             ", wyśrodkowane

print(liczba)  # 456789123690
print(f"Nasza duża liczba {liczba:,}")  # Nasza duża liczba 456,789,123,690
print(f"Nasza duża liczba {liczba:_}")  # Nasza duża liczba 456_789_123_690
print(f"Nasza duża liczba {liczba:_}".replace("_", " "))  # Nasza duża liczba 456 789 123 690

liczba2 = 15000000000000
liczba3 = 15_000_000_000_000
print(type(liczba3))  # <class 'int'>
print(liczba3)  # 15000000000000
