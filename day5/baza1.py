# bazy danych - przechowują zbiory danych
# baza danych ma silnik do działań z danymi
# relacyjne, nieralacyjne sql, nosql
# postgres, mysql, oracle
import sqlite3  # biblioteka do bazy danych

try:
    conn = sqlite3.connect('baza_danych.db')
    c = conn.cursor()
    print("Baza podłączona prawidłowo")
except sqlite3.Error as e:
    print("Błąd podłączenia bazy danych", e)
finally:
    if conn:
        conn.close()
        print("Połaczenie zostało zamknięte")
