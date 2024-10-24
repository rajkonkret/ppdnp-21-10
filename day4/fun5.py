# stworzyc funkcję obliczającą średnią
def liczymy(name=None, *cyfry):  # dowolna ilość argumentów pozycyjnych
    print(cyfry)
    count = len(cyfry)  # liczba elementów
    suma = 0
    suma_p = sum(cyfry)
    print(suma_p)
    try:
        for c in cyfry:
            suma += c
        avg = count / suma
    except Exception as e:
        print("Bład", e)
    else:
        print(f"Średnia dla ucznia {name} wynosi {avg}")
    finally:
        print("Kolejny uczeń")


liczymy()
liczymy(1)
liczymy(1, 2)
liczymy(1, 2, 3)
liczymy(1, 2, 3, 5, 5, 6)
liczymy("Radek", 5, 6, 6, 6, 5, 5)
# ()
# (1,)
# (1, 2)
# (1, 2, 3)
# (1, 2, 3, 5, 5, 6)
# ()
# Bład division by zero
# Kolejny uczeń
# (1,)
# Średnia wynosi 1.0
# Kolejny uczeń
# (1, 2)
# Średnia wynosi 0.6666666666666666
# Kolejny uczeń
# (1, 2, 3)
# Średnia wynosi 0.5
# Kolejny uczeń
# (1, 2, 3, 5, 5, 6)
# Średnia wynosi 0.2727272727272727
# Kolejny uczeń
a, *b = "Radek", 5, 5, 5
print(a, b)  # Radek [5, 5, 5]
# ()
# Bład division by zero
# Kolejny uczeń
# ()
# Bład division by zero
# Kolejny uczeń
# (2,)
# Średnia dla ucznia 1 wynosi 0.5
# Kolejny uczeń
# (2, 3)
# Średnia dla ucznia 1 wynosi 0.4
# Kolejny uczeń
# (2, 3, 5, 5, 6)
# Średnia dla ucznia 1 wynosi 0.23809523809523808
# Kolejny uczeń
# (5, 6, 6, 6, 5, 5)
# Średnia dla ucznia Radek wynosi 0.18181818181818182
# Kolejny uczeń
# 33
# Średnia dla ucznia Radek wynosi 0.18181818181818182
# Kolejny uczeń
# Radek [5, 5, 5]
