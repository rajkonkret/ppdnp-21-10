import pandas as pd

excel_data = pd.read_excel('courses.xlsx')

print(excel_data)
#    Unnamed: 0 Courses    Fee Duration  Discount
# 0           0   Spark  25000  50 Days      2000
# 1           1  Pandas  20000  30 Days      1500
# 2           2  Python  15000      NaN       800
# 3           3     PHP  18000  15 Days       500

data = pd.DataFrame(excel_data)
print(data.columns)  # Index(['Unnamed: 0', 'Courses', 'Fee', 'Duration', 'Discount'], dtype='object')
print(data.items)
# <bound method DataFrame.items of    Unnamed: 0 Courses    Fee Duration  Discount
# 0           0   Spark  25000  50 Days      2000
# 1           1  Pandas  20000  30 Days      1500
# 2           2  Python  15000      NaN       800
# 3           3     PHP  18000  15 Days       500>

print(data.values)
# [[0 'Spark' 25000 '50 Days' 2000]
#  [1 'Pandas' 20000 '30 Days' 1500]
#  [2 'Python' 15000 nan 800]
#  [3 'PHP' 18000 '15 Days' 500]]

print(data.index[-1])  # index 3
print(data.columns[1])  # Courses

print(data[data['Fee'] > 20000])
#    Unnamed: 0 Courses    Fee Duration  Discount
# 0           0   Spark  25000  50 Days      2000
