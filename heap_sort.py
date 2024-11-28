import time
import random


def heapify(arr, n, i):
    largest = i  # inicializar el mayor como raiz
    left = 2 * i + 1  # hijo izquierdo
    right = 2 * i + 2  # hijo derecho

    # si hijo izquierdo es mayor que la raiz
    if left < n and arr[left] > arr[largest]:
        largest = left

    # si el hijo derecho es mayor que el mayor 
    if right < n and arr[right] > arr[largest]:
        largest = right

    # si el mayor no es la raiz
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # intercambiar
        # recursivamente aplicar heapify 
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)

    #  heap max
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # extraer elementos del heap 
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # mover la raiz al final
        heapify(arr, i, 0)

    return arr

# funcion para medir tiempo de ejecucion
def measure_heap_sort():
    input_sizes = [10, 100, 1000, 5000, 10000, 20000, 1000000]  # tamaños de array
    for size in input_sizes:
        # generar array aleatorio para probar
        test_array = [random.randint(0, 100000) for _ in range(size)]
        start_time = time.time()
        heap_sort(test_array.copy())
        end_time = time.time()
        time_taken = end_time - start_time
        print(f"Array Size: {size}, Time Taken: {time_taken:.6f} seconds")

# ejecutar la funcion de tiempo
if __name__ == "__main__":
    measure_heap_sort()
