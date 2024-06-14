import sys
from algs import *
from inputy import *
info = """przekaż do stdin informacje w formacie:
          
Pierwsza linia pliku określa pojemność plecaka (C), czyli ile maksymalnie przedmiotów możesz zapakować.

Druga linia określa liczbę przedmiotów (n), które chcesz rozważyć w plecaku.

Każda kolejna linia zawiera wartość (pi) i objętość (wi) jednego z przedmiotów.


program należy wywołać:

python3 main.py dynamic             -dla rozwiązywania algorytmem dynamicznym

python3 main.py brute               -dla rozwiązywania algorytmem bruteforce
"""

def main():
    try:
        if sys.argv[1] == "dynamic":
            # Wczytanie danych z stdin i wywołanie algorytmu programowania dynamicznego
            C, n, values, weights = read_input_stdin()
            max_value, items = dynamic(C, weights, values, n)
            print("Algorytm programowania dynamicznego:")
            print("Maksymalna wartość:", max_value)
            print("Indeksy przedmiotów:", items)
        elif sys.argv[1] == "brute":
            # Wczytanie danych z stdin i wywołanie algorytmu brute force
            C, n, values, weights = read_input_stdin()
            max_value, items = brute(C, weights, values, n)
            print("\nAlgorytm brute force:")
            print("Maksymalna wartość:", max_value)
            print("Indeksy przedmiotów:", items)
        else:
            print(info)

    except:
        print(info)


if __name__ == '__main__':
    main()
    

