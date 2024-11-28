import time
import random


def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        # ultimos i elementos ya estan ordenados
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                # intercambiar si el elemento actual es mayor al siguiente
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

# funcion para medir tiempo de ejecucion
def measure_bubble_sort():
    input_sizes = [10, 100, 1000, 5000, 10000,20000]  # tamaños de array
    for size in input_sizes:
        # generar array aleatorio para probar
        test_array = [random.randint(0, 100000) for _ in range(size)]
        start_time = time.time()
        bubble_sort(test_array.copy())
        end_time = time.time()
        time_taken = end_time - start_time
        print(f"Array Size: {size}, Time Taken: {time_taken:.6f} seconds")

# ejecutar la funcion de tiempo
if __name__ == "__main__":
    measure_bubble_sort()
