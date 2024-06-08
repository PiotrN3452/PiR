import os

def generate_file(file_path, n, random_data=True):
    with open(file_path, 'w') as file:
        file.write(f"{n}\n")  # Pierwsza linia: liczba od 16 do 2^18
        file.write("0.3\n")   # Druga linia: 0.3
        file.write("hamilton\n")
        #file.write("print\n") # Trzecia linia: print

        # Jeśli `random_data` jest ustawione na True, to dodaj losowe dane
        if random_data:
            for number in range(1, n + 1):
                file.write(f"{number}\n")


def main():
    folder_name = "benchmark4"
    os.makedirs(folder_name, exist_ok=True)
    
    # Iteracja od 16 do 262144
    for i in range(4, 19):  # 2^5 = 32, 2^18 = 262144
        n = 2 ** i
        print(f"Generowanie pliku dla n = {n}")

        # Tworzenie pliku dla każdej wartości n
        file_name = f"file_{n}.txt"
        file_path = os.path.join(folder_name, file_name)
        generate_file(file_path, n, random_data=False)

if __name__ == "__main__":
    main()