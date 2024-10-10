"""Napisz program, które pobierze liczbę naturalną n, a następnie wyświetli macierz sąsiedztwa wypełnione zerami rozmiaru n×n.
 W przypadku podania złej liczby program ma wypisać komunikat BŁĄD oraz zakończyć działanie."""

import sys

def emptymatrix(length):
    matrix = [['0' for space in range(length)] for rows in range(length)]
    for row in matrix:
        print(' '.join(x for x in row))
try:
    n = input()
except EOFError:
    print("BŁĄD")
    sys.exit()
try:
    n = int(n)
except ValueError:
    print("BŁĄD")
    sys.exit()
if n <= 0:
    print("BŁĄD")
    sys.exit()
emptymatrix(n)



    


