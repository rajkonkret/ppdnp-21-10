# funkcja wewnętrzna, zagnieżdzona
# używane w dekoratorach
def fun1():
    print("To jest fun1")

    def fun2():
        print("To jest fun2")

    return fun2  # zwraca adres funkcji - referencję, bez nawiasów


fun1()
xFun = fun1()  # To jest fun1
# zmienna xFun przechowuje adres funkcji fun2
# w takim przypadku możemy uruchomic tą funkcję za pomocą ()
print(xFun)  # <function fun1.<locals>.fun2 at 0x000001F683A19C60>
print(type(xFun))  # <class 'function'>
xFun()  # To jest fun2
