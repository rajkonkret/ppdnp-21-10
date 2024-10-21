tekst = "Witaj Świecie"
print(tekst)
print(type(tekst))
# Witaj Świecie
# <class 'str'>

# teksty są niemutowalne
tekst.upper()
""" Return a copy of the string converted to uppercase. """
print(tekst.upper())  # WITAJ ŚWIECIE
print(tekst.upper())

tekst_upper = tekst.upper()
print(tekst_upper)

print(tekst.lower())  # witaj świecie
print(tekst)  # Witaj Świecie

# Witaj Świecie
# 0123456789...
print(tekst[1])  # "i" - indeks 1 , druga literka w szeregu

print(tekst.count("i"))  # występuje 3 razy
print(tekst.count("j", 0, 4))  # 0 razy, z prawej zbiór otwarty, weźmie 0123, "j", 0, 4

print(tekst.removeprefix("Witaj"))  # " Świecie"
print(tekst.removesuffix("Świecie"))  # "Witaj "

tekst_zamiana = "Witaj dobry Świecie"
print(tekst_zamiana.replace("dobry", ""))  # "Witaj  Świecie"
print(tekst.removesuffix("Świecie").strip())  # "Witaj", usunie białe znaki, wiodące i kończące spacje

# kodowanie znaków
encode_s = tekst.encode('utf-8')
print(encode_s)  # b'Witaj \xc5\x9awiecie'
# b - typ bajtowy
# \xc5\x9a - zapis szesnastkowy, \xc5 197
print(type(encode_s))  # <class 'bytes'>

print(encode_s.decode('utf-8'))  # Witaj Świecie

print("\a")

imie = "Radek"
# f - string - sformatowane teksty
tekst_format = f"Mam na imię {imie} i lubię pythona."
print(tekst_format)  # Mam na imię Radek i lubię pythona.

tekst_format2 = f"\tMam na imię {imie}\n i lubię pythona.\b"
tekst_format3 = f"\t Mam na imię {imie}\n i lubię pythona.\b"
print(tekst_format2)  # "	 ","	"
print(tekst_format3)  # "	 ","	"
# "Mam na imię Radek i lubię pythona.
# 	Mam na imię Radek
#  i lubię pythona
# 	 Mam na imię Radek
#  i lubię pythona"
# "	Mam na imię Radek
#  i lubię pythona"

starszy = "Witaj %s!"  # %s - %s - łańcuch znaków (string)
print(starszy % imie)  # Witaj Radek!

print("Witaj {}!".format(imie))  # Witaj Radek!

# tekst wielolinijkowy
print("""Tekst
    wielolinijkowy""")
# "Tekst
#     wielolinijkowy"

print(len(tekst_format2))  # długość 37
print(len(tekst_format3))  # długość 38
