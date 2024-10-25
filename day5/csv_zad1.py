# pliki csv - dane w pliku odzdielone znakiem podziału
# 1,john,2000,sales
# 11,Andrew,5000,finance
# 21,Mark,8000,hr

import csv
from dataclasses import fields

fields = ['name', 'branch', 'year', 'cgpa']
row = ['Radek', "Coe", 2, '9.1']

dictionary = dict(zip(fields, row))
print(dictionary)
# {'name': 'Radek', 'branch': 'Coe', 'year': 2, 'cgpa': '9.1'}

filename = 'records.csv'
with open(filename, "w", newline="") as csv_f:
    cswriter = csv.writer(csv_f)
    cswriter.writerow(fields)
    cswriter.writerow(row)

filename = 'records_2.csv'
with open(filename, "w", newline="") as f:
    csvwriter = csv.DictWriter(f, fieldnames=fields)
    csvwriter.writeheader()
    csvwriter.writerow(dictionary)

products = [
    {'sku': 1, 'exp_date': "today", 'price': 100},
    {'sku': 2, 'exp_date': "today", 'price': 200},
    {'sku': 3, 'exp_date': "tomorrow", 'price': 150},
    {'sku': 4, 'exp_date': "today", 'price': 50.00},
    {'sku': 5, 'exp_date': "tomorrow", 'price': 90},
]

fields_product = ['sku', 'exp_date', 'price']
filename = 'records_3.csv'
with open(filename, "w", newline="") as f:
    csvwriter = csv.DictWriter(f, fieldnames=fields_product, delimiter=";")
    csvwriter.writeheader()
    csvwriter.writerows(products)  # writerows - zapisuje listę
