from abc import ABC, abstractmethod


class Ptak(ABC):
    """
    Klasa opisująca ptaka w pythonie
    """

    def __init__(self, gatunek, szybkosc):
        """
        Metoda inicjalizująca
        :param gatunek:
        :param szybkosc:
        """
        self.gatunek = gatunek
        self.szybkosc = szybkosc

    def latam(self):
        print("Tu", self.gatunek, "Lecę z szybkością", self.szybkosc)

    # metoda abstrakcyjna
    @abstractmethod
    def wydaj_odglos(self):
        pass


class Kura(Ptak):  # klasa Kura dziedziczy po Ptak
    """
    Klasa Kura
    """

    def __init__(self, gatunek):
        super().__init__(gatunek, 0)  # musimy wywołac konstruktor klasy wyzszej, super() - klasa wyzsza

    def latam(self):
        print("Tu", self.gatunek, "Ja nie latam.")

    def wydaj_odglos(self):
        print("Ko ko ko ko")

    def dziobanie(self):
        print("Idę sobie podziobać")


class Orzel(Ptak):
    """
    Klasa Orzel dziedziczy po Ptak
    """

    def wydaj_odglos(self):
        print("Kier kir kier")

    def polowanie(self):
        print("Rozpoczynam polowanie")


class Sowa(Ptak):
    """
    Klasa Sowa
    """


# po oznaczeniu klasy jako abstrakcyjna nie możemy stworzyć obiektu klasy Ptak
# Traceback (most recent call last):
#   File "C:\Users\CSComarch\PycharmProjects\ppdnp-21-10\day5\kl3.py", line 37, in <module>
#     or1 = Ptak("Orzel", 45)
#           ^^^^^^^^^^^^^^^^^
# TypeError: Can't instantiate abstract class Ptak without an implementation for abstract method 'wydaj_odglos'

# or1 = Ptak("Orzel", 45)
# or1.latam()  # Tu Orzel Lecę z szybkością 45
# kur1 = Ptak("Kura", 0)
# kur1.latam()  # Tu Kura Lecę z szybkością 0

kur2 = Kura("Kura domowa")
kur2.latam()  # Tu Kura domowa Ja nie latam.
kur2.wydaj_odglos()  # Ko ko ko ko

or2 = Orzel("Orzel Bielik", 50)
or2.latam()
or2.wydaj_odglos()
# Tu Orzel Bielik Lecę z szybkością 50
# Kier kir kier
or2.polowanie()
# Rozpoczynam polowanie

kur2.dziobanie()  # Idę sobie podziobać

# obiekty róznych klas
# klasy dzidziczą po klasie Ptak
# dzieki wymuszeniu nadpisania  metody abstrakcyjnej we wszystkich dziedziczących
# możemy w zakresie tej metody traktować je jakby były obiektami tej samej klasy
# to się nazywa polimorfizm
lista = [kur2, or2]
for i in lista:
    i.wydaj_odglos()
# Ko ko ko ko
# Kier kir kier


# nie stworzymy obiektu klasy Sowa bo nie ma metody wydaj_odglos
# sowa = Sowa("Sowa", 20)
# Traceback (most recent call last):
#   File "C:\Users\CSComarch\PycharmProjects\ppdnp-21-10\day5\kl3.py", line 100, in <module>
#     sowa = Sowa("Sowa", 20)
#            ^^^^^^^^^^^^^^^^
# TypeError: Can't instantiate abstract class Sowa without an implementation for abstract method 'wydaj_odglos'