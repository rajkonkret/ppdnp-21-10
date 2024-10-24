import chardet

# pip install chardet - wpisujemy w terminalu
with open('test.log', "r", encoding='utf-8') as f:
    raw_data = f.read()

print(raw_data)
# Nadpisane
# Dopisane
# Dopisane
# Dodane
# Dośdane

# rb - odczyt binarny
with open('test.log', 'rb') as f:
    raw_data = f.read()

result = chardet.detect(raw_data)
print(result)
# {'encoding': 'Windows-1254', 'confidence': 0.6623585739772819, 'language': 'Turkish'}
# po zwiększeniu próbki (więcej polskich znaków w tekście)
# {'encoding': 'utf-8', 'confidence': 0.99, 'language': ''}
encoding = result['encoding']
print("Kodowanie znaków:", encoding)  # Kodowanie znaków: utf-8
print(raw_data.decode(encoding=encoding))  # encoding='utf-8'
# Nadpisane
# Dopisane
# Dopisane
# Dodane
# Dośdane
# Dośćążdane
