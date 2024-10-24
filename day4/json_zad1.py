# json - '{"name":"John", "age":30, "car":null}'
# dane typu klucz-wartosc
# uzywane do komunikacji w systemach w internecie
import json
from textwrap import indent

person_dict = {'name': "Radek", 'age': 48, "czy_pali": None}
print(type(person_dict))  # <class 'dict'>

with open('nasze_dane.json', "w") as f:
    json.dump(person_dict, f)

# upiększają
with open('nasze_dane.json', "w") as f:
    json.dump(person_dict, f, indent=4)
# {
#     "name": "Radek",
#     "age": 48,
#     "czy_pali": null
# }

with open('nasze_dane.json', "w") as f:
    json.dump(person_dict, f, indent=4, sort_keys=True)
# {
#     "age": 48,
#     "czy_pali": null,
#     "name": "Radek"
# }

# wczytanie pliku
with open('nasze_dane.json', 'r') as f:
    data = json.load(f)

print(data)
print(type(data))
# {'age': 48, 'czy_pali': None, 'name': 'Radek'}
# <class 'dict'>
print(data['name'])  # Radek

# zamiana słownik na json (text)
json_text = json.dumps(data)
print(type(json_text))
print(json_text)
# <class 'str'>
# {"age": 48, "czy_pali": null, "name": "Radek"}

# wczytanie jsona (text) do słownika
dict_json = json.loads(json_text)
print(dict_json)
print(type(dict_json))
# {'age': 48, 'czy_pali': None, 'name': 'Radek'}
# <class 'dict'>

for key in dict_json:
    print(key)
# age
# czy_pali
# name

print(dict_json.keys())  # dict_keys(['age', 'czy_pali', 'name'])
