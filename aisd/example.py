import sys
import random
sys.setrecursionlimit(999999999)








   







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


def quick_sort_lp(A, p, r): # --algorithm 4
    if p < r:
        q = partition_lp(A, p, r)
        quick_sort_lp(A, p, q)
        quick_sort_lp(A, q + 1, r)
def partition_lp(A, p, r):
    pi = p  
    c = A[pi]
    i = p
    for j in range(p + 1, r + 1):
        if A[j] < c:
            i += 1
            A[i], A[j] = A[j], A[i]
    pfi = i
    A[pi], A[pfi] = A[pfi], A[pi]
    return pfi



def quick_sort_rp(A, p, r):  # --algorithm 5
    if p < r:
        q = partition_rp(A, p, r)
        quick_sort_rp(A, p, q)
        quick_sort_rp(A, q + 1, r)
def partition_rp(A, p, r):
    pi = random.randint(p, r)  
    A[p], A[pi] = A[pi], A[p]  
    pivot_value = A[p]
    i = p
    for j in range(p + 1, r + 1):
        if A[j] < pivot_value:
            i += 1
            A[i], A[j] = A[j], A[i]
    pfi = i
    A[p], A[pfi] = A[pfi], A[p]
    return pfi


def max_heapify(a, heap_size, i):
    l = 2 * i + 1
    r = 2 * i + 2
    largest = i
    if l < heap_size and a[l] > a[largest]:
        largest = l
    if r < heap_size and a[r] > a[largest]:
        largest = r
    if largest != i:
        a[i], a[largest] = a[largest], a[i]
        max_heapify(a, heap_size, largest)
        
def build_max_heap(a):
    heap_size = len(a)
    for i in range(heap_size // 2 - 1, -1, -1):
        max_heapify(a, heap_size, i)

def heap_sort(a):
    build_max_heap(a)
    heap_size = len(a)
    for i in range(heap_size - 1, 0, -1):
        a[0], a[i] = a[i], a[0]
        heap_size -= 1
        max_heapify(a, heap_size, 0)



def quick_sort_descending(A, p, r): #--algorithm 7
    if p < r:
        q = partition_descending(A, p, r)
        quick_sort_descending(A, p, q)
        quick_sort_descending(A, q + 1, r)

def partition_descending(A, p, r):
    pi = p
    c = A[pi]
    i = p
    for j in range(p + 1, r + 1):
        if A[j] > c:
            i += 1
            A[i], A[j] = A[j], A[i]
    pfi = i
    A[pi], A[pfi] = A[pfi], A[pi]
    return pfi



def sort_using_algorithm(data, algorithm): 
    if algorithm == 1:  
        insertion_sort(data)
    elif algorithm == 2:
        shell_sort(data)
    elif algorithm == 3:
        selection_sort(data)
    elif algorithm == 5:
        quick_sort_lp(data,0,len(data)-1)
    elif algorithm == 6:
        quick_sort_rp(data,0,len(data)-1)
    elif algorithm == 4:
        heap_sort(data)
    elif algorithm == 7:
        quick_sort_descending(data,0,len(data)-1)
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