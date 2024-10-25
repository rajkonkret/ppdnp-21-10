import pandas

# pip instal pandas

data = pandas.read_csv('records_2.csv')
print(data)
#     name branch  year  cgpa
# 0  Radek    Coe     2   9.1
print(data.columns)
# Index(['name', 'branch', 'year', 'cgpa'], dtype='object')
print(data.values)
# [['Radek' 'Coe' 2 9.1]]

data_delimiter = pandas.read_csv('records_3.csv', delimiter=";")
print(data_delimiter)
#    sku  exp_date  price
# 0    1     today  100.0
# 1    2     today  200.0
# 2    3  tomorrow  150.0
# 3    4     today   50.0
# 4    5  tomorrow   90.0