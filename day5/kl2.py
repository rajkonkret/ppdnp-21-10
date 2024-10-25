class Human:
    """
    Klasa Human opisująca człowieka w pythonie
    """

    def __init__(self, imie, wiek, wzrost, plec="k"):
        """
        Metoda inicjalizująca (konstruktor)
        self - obiekt np.: cz1
        :param imie:
        :param wiek:
        :param wzrost:
        :param plec:
        """
        self.imie = imie
        self.wiek = wiek
        self.wzrost = wzrost
        self.plec = plec

    def powitanie(self):
        print(f"Nazywam się {self.imie}")

    # dopisac metody
    # wypisz_wiek, wypisz_wzrost
    def wypisz_wiek(self):
        print(f"Mam {self.wiek} lat.")

    def wypisz_wzrost(self):
        print(f"Mam {self.wzrost} cm wzrostu.")

    def ruszaj(self):
        if self.plec == "k":
            print("Ruszyłam w drogę")
        else:
            print("Ruszyłem w drogę")


# TypeError: Human.__init__() missing 3 required positional arguments: 'imie', 'wiek', and 'wzrost'
# cz1 = Human()

cz1 = Human("Anna", 27, 168)
print(cz1.imie)
print(cz1.wiek)
print(cz1.wzrost)
print(cz1.plec)
# Anna
# 27
# 168
# k
# uruchomienie metody na obiekcie
# obiekt cz1
cz1.powitanie()
# Anna
# 27
# 168
# k
# Nazywam się Anna

cz2 = Human("Radek", 50, 193, "m")
print(cz2.imie)
print(cz2.wiek)
print(cz2.wzrost)
print(cz2.plec)
cz2.powitanie()
# Radek
# 50
# 193
# m
# Nazywam się Radek
cz2.wypisz_wiek()
cz2.wypisz_wzrost()

cz1.wypisz_wiek()
# Nazywam się Radek
# Mam 50 lat.
# Mam 193 cm wzrostu.
# Mam 27 lat.

cz1.ruszaj()
cz2.ruszaj()
# Ruszyłam w drogę
# Ruszyłem w drogę