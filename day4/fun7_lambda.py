# funkcja lambda
# skrócony zapis funkcji
# zwraca wynik
# funkcja anonimowa, możliwosc uzycia w miejscu deklaracji
def odejmij(a, b):
    return a - b


print(odejmij(123, 56))  # 67

odejmij2 = lambda a, b: a - b
print(odejmij2(123, 56))  # 67

wiek = lambda x: "dziecko" if x < 10 else ("nastolatek" if x < 18 else "dorosły")
print(wiek(9))  # dziecko
print(wiek(10))  # nastolatek
print(wiek(17))  # nastolatek
print(wiek(18))  # dorosły
print(wiek(25))  # dorosły

lista = [1, 2, 3, 10, 20, 50, 70, 200, 300, 500]

lista_wyn = []
for i in lista:
    lista_wyn.append(i * 2)
print(lista_wyn)  # [2, 4, 6, 20, 40, 100, 140, 400, 600, 1000]

print([i * 2 for i in lista])  # [2, 4, 6, 20, 40, 100, 140, 400, 600, 1000]
