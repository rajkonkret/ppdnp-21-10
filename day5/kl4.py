# hermetyzacja - odizolowanie od zewnętrznego śrdowiska

class Car:
    """
    Klasa opisująca samochód w pythonie
    """

    def __init__(self, model, year):
        # uzupełnijcie konstruktor
        self.model = model
        self.year = year
        # pole prywatne
        self.__predkosc = 0

    def gaz(self):
        self.__predkosc += 10

    def licznik(self):
        print(f"Prędkość wynosi {self.__predkosc} km/h")

    def hamuj(self):
        self.__predkosc -= 10
        self.__zmiana_biegu()

    # metoda prywatna
    def __zmiana_biegu(self):
        print("Zmiana biegu")


car = Car("Maluch", 2024)
car.gaz()
car.gaz()
car.gaz()
car.gaz()
car.gaz()
# print(car.__predkosc)  # 50, AttributeError: 'Car' object has no attribute '__predkosc'. Did you mean: '_Car__predkosc'?
car.licznik()  # Prędkość wynosi 50 km/h
# car.__predkosc = 0
car.hamuj()
car.hamuj()
car.hamuj()
car.hamuj()
car.hamuj()
car.licznik()  # Prędkość wynosi 0 km/h
# Prędkość wynosi 50 km/h
# Zmiana biegu
# Zmiana biegu
# Zmiana biegu
# Zmiana biegu
# Zmiana biegu
# Prędkość wynosi 0 km/h
