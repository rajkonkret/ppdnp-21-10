# bazy danych - przechowują zbiory danych
# baza danych ma silnik do działań z danymi
# relacyjne, nieralacyjne sql, nosql
# postgres, mysql, oracle
import sqlite3  # biblioteka do bazy danych

try:
    conn = sqlite3.connect('baza_danych.db')
    c = conn.cursor()
    print("Baza podłączona prawidłowo")

    query = """
    CREATE TABLE IF NOT EXISTS developers (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    salary REAL NOT NULL);
    """

    c.execute(query)
    conn.commit()

    # insert = """
    # INSERT INTO developers (id,name,email,salary) VALUES (1,'Radek','radek@radek.pl','10000');
    # """
    insert = """
    INSERT INTO developers (id,name,email,salary) VALUES (2,'Radek','radek2@radek.pl','10000');
    """
    # c.execute(insert)
    # conn.commit()

    select = "SELECT * FROM developers;"
    for row in c.execute(select):
        print(row)

except sqlite3.Error as e:
    print("Błąd podłączenia bazy danych", e)
finally:
    if conn:
        conn.close()
        print("Połaczenie zostało zamknięte")
# Baza podłączona prawidłowo
# (2, 'Radek', 'radek2@radek.pl', 10000.0)
# Połaczenie zostało zamknięte
