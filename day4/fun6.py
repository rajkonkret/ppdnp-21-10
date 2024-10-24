# argumenty po nazwie
def connect(**opcje):  # ** dowolna ilość argumentów po nazwie
    print(opcje)
    print(type(opcje))  # <class 'dict'>


connect(a=90)  # {'a': 90}
connect(b=19, c=90, name="Radek")


# ta funkcja przyjmie dowolną ilość argumentów pozycyjnych
# i dowolną ilość argumentów nazwanych
def all_params(*args, **kwargs):
    print(args, kwargs)


all_params(1, 2, 3, 4, 5, 6)
all_params(1, 2)
all_params(a=9, b=10, c=8, z=99)
# (1, 2, 3, 4, 5, 6) {}
# (1, 2) {}
# () {'a': 9, 'b': 10, 'c': 8, 'z': 99}
all_params(1, 2, c=90, name="Radek")
# (1, 2) {'c': 90, 'name': 'Radek'}
all_params()  # () {}
