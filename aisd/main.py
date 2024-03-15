import sys

def insertion_sort(data): # --algorithm 1
    for i in range(1, len(data)):
        key = data[i]
        j = i - 1
        while j >= 0 and key < data[j]:
            data[j + 1] = data[j]
            j -= 1
        data[j + 1] = key

def shell_sort(data): # --algorithm 2 
    n = len(data)  
    k = n // 2 
    x = 0
    while k > 0:
        for a in range(k):
            data_n = [data[i] for i in range(0,len(data),k)]
            insertion_sort(data_n)
            for i in range(0,len(data_n)):
                data[x] = data_n[i]
                x = x + k
            x = 0
            i = i+1
        k = k // 2  
    return data

def selection_sort(data): # --algorithm 3
    for j in range(0, len(data)-1): 
        min = j 
        for i in range(j+1,len(data)):
            if data[i] < data[min]:
                min = i
        if min != j:
            data[min], data[j] = data[j], data[min]
    return data

def sort_using_algorithm(data, algorithm): 
    if algorithm == 1:  
        insertion_sort(data)
    elif algorithm == 2:
        shell_sort(data)
    elif algorithm == 3:
        selection_sort(data)
    else:
        # Default to using the sorted function if the algorithm number is not recognized
        data = sorted(data)
    return data

def main():
    # Command-line arguments: python script.py --algorithm <algorithm_number>
    if len(sys.argv) != 3 or sys.argv[1] != "--algorithm":
        print("Usage: python script.py --algorithm <algorithm_number>")
        sys.exit(1)

    algorithm_number = int(sys.argv[2])

    # Read input data from standard input until the end of file (EOF)
    input_data = sys.stdin.read().split()
    try:
        data = [int(x) for x in input_data[1:]]
    except EOFError:
        print("Error reading input.")

    # Perform sorting using the specified algorithm
    sorted_data = sort_using_algorithm(data, algorithm_number)

    # Print the sorted data
    print("Sorted data:", sorted_data[0:10])

if __name__ == "__main__":
    main()