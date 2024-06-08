import sys



def knapsack_dynamic(C, weights, values, n):
    # Inicjalizacja tablicy pomocniczej dla przechowywania wyników
    K = [[0 for _ in range(C + 1)] for _ in range(n + 1)]

    # Wypełnianie tablicy pomocniczej zgodnie z algorytmem programowania dynamicznego
    for i in range(n + 1):
        for w in range(C + 1):
            if i == 0 or w == 0:
                K[i][w] = 0
            elif weights[i - 1] <= w:
                K[i][w] = max(values[i - 1] + K[i - 1][w - weights[i - 1]], K[i - 1][w])
            else:
                K[i][w] = K[i - 1][w]

    # Pętla do odtworzenia wybranych przedmiotów
    result = []
    w = C
    for i in range(n, 0, -1):
        if K[i][w] != K[i - 1][w]:
            result.append(i)
            w -= weights[i - 1]

    return K[n][C], result

def knapsack_brute_force(C, weights, values, n):
    def knapsack_recursive(C, weights, values, n):
        if n == 0 or C == 0:
            return 0, []

        if weights[n - 1] > C:
            return knapsack_recursive(C, weights, values, n - 1)
        
        without_current_item, without_indices = knapsack_recursive(C, weights, values, n - 1)
        with_current_item, with_indices = knapsack_recursive(C - weights[n - 1], weights, values, n - 1)
        with_current_item += values[n - 1]

        if with_current_item > without_current_item:
            return with_current_item, with_indices + [n]
        else:
            return without_current_item, without_indices

    max_value, items = knapsack_recursive(C, weights, values, n)
    return max_value, list(reversed(items))

def read_input(filename):
    with open(filename, 'r') as file:
        C = int(file.readline())
        n = int(file.readline())
        values = []
        weights = []
        for _ in range(n):
            line = file.readline().split()
            values.append(int(line[0]))
            weights.append(int(line[1]))
    return C, n, values, weights

try:
    if sys.argv[1] == "dynamic":

    # Wczytanie danych z pliku i wywołanie algorytmu programowania dynamicznego
        C, n, values, weights = read_input('data.txt')
        max_value, items = knapsack_dynamic(C, weights, values, n)
        print("Algorytm programowania dynamicznego:")
        print("Maksymalna wartość:", max_value)
        print("Indeksy przedmiotów:", items)
    elif sys.argv[1] == "brute":
    # Wczytanie danych z pliku i wywołanie algorytmu brute force
        C, n, values, weights = read_input('data.txt')
        max_value, items = knapsack_brute_force(C, weights, values, n)
        print("\nAlgorytm brute force:")
        print("Maksymalna wartość:", max_value)
        print("Indeksy przedmiotów:", items)
    else:
        print("""utwóż plik data.txt w którym podasz dane w formacie:
          
Pierwsza linia pliku określa pojemność plecaka (C), czyli ile maksymalnie przedmiotów możesz zapakować.

Druga linia określa liczbę przedmiotów (n), które chcesz rozważyć w plecaku.

Każda kolejna linia zawiera wartość (pi) i objętość (wi) jednego z przedmiotów.


program należy wywołać:

python3 main.py dynamic             -dla rozwiązywania algorytmem dynamicznym

python3 main.py brute               -dla rozwiązywania algorytmem bruteforce
""")

except:
    print("""utwóż plik data.txt w którym podasz dane w formacie:
          
Pierwsza linia pliku określa pojemność plecaka (C), czyli ile maksymalnie przedmiotów możesz zapakować.

Druga linia określa liczbę przedmiotów (n), które chcesz rozważyć w plecaku.

Każda kolejna linia zawiera wartość (pi) i objętość (wi) jednego z przedmiotów.

program należy wywołać:

python3 main.py dynamic             -dla rozwiązywania algorytmem dynamicznym

python3 main.py brute               -dla rozwiązywania algorytmem bruteforce
""")
