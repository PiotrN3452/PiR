import os
import subprocess
import time

def run_main4(file_path):
    # Budowanie komendy do wykonania
    command = f"python3 /mnt/c/Users/ryshi/Desktop/PiR/aisd_4/main4.py --hamilton < {file_path}"
    
    # Pomiar czasu wykonania
    start_time = time.time()
    subprocess.run(command, shell=True)
    end_time = time.time()

    # Obliczanie czasu wykonania i wyświetlanie
    execution_time = end_time - start_time
    print(f"Czas wykonania dla pliku {file_path}: {execution_time} sekund")

def main():
    folder_name = "benchmark4"
    
    # Iteracja przez pliki w folderze
    for i in range(4, 19):  # Zakres od 1024 (2^10) do 262144 (2^18)
        n = 2 ** i
        file_name = f"file_{n}.txt"
        file_path = os.path.join(folder_name, file_name)
        if os.path.isfile(file_path):
            print(f"Uruchamianie dla pliku: {file_name}")
            run_main4(file_path)

if __name__ == "__main__":
    main()