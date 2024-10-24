from datetime import date, datetime, timedelta

today = date.today()
print(today)  # 2024-10-24
print(type(today))  # <class 'datetime.date'>

time = datetime.now()
print("Aktualny czas:", time)  # Aktualny czas: 2024-10-24 09:22:11.671808

# tomorrow = today + 1  # TypeError: unsupported operand type(s) for +: 'datetime.date' and 'int'
# days=0, seconds=0, microseconds=0,
#                 milliseconds=0, minutes=0, hours=0, weeks=0
# dla lat juz inna biblioteka np.: dateutil
tomorrow = today + timedelta(days=1)
print(tomorrow)  # 2024-10-25

print(time.time())
print(today.day)
print(time.hour)
# 09:31:20.386841
# 24
# 9

formatted_date = datetime.now().strftime("%d/%m/%Y")
print(formatted_date)  # 24/10/2024

# wypisac godzine w formacie 9:22
formatted_time = datetime.now().strftime("%H:%M")
print(formatted_time)  # 09:35

# 12h
formatted_time_12h = datetime.now().strftime("%I:%M %p")
print(formatted_time_12h)  # 09:36 AM
print(type(formatted_time_12h))  # <class 'str'>

# zamiana stringa na datatime
data_object = datetime.strptime("24/10/2024", "%d/%m/%Y")
print(data_object)  # 2024-10-24 00:00:00
print(type(data_object))  # <class 'datetime.datetime'>

products = [
    {'sku': 1, 'exp_date': today, 'price': 100},
    {'sku': 2, 'exp_date': today, 'price': 200},
    {'sku': 3, 'exp_date': tomorrow, 'price': 150},
    {'sku': 4, 'exp_date': today, 'price': 50.00},
    {'sku': 5, 'exp_date': tomorrow, 'price': 90},
]

for i in products:
    # print(i)
    # print(type(i))
    # i['price']
    # i['exp_date']
    if i['exp_date'] != today:
        continue  # wraca na początek pętli, bierze kolejny element
    i['price'] *= 0.8  # p = p * 0.8
    print(f"""Price for sku {i['sku']}
is now {i['price']}""")
# Price for sku 1
# is now 80.0
# Price for sku 2
# is now 160.0
# Price for sku 4
# is now 40.0
