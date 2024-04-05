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

# Przykładowe użycie:
array = [12, 51, 43, 52, 96, 70]
heap_sort(array)
print("Posortowana tablica:")
print(array)
