import time
import random

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]  # seleccionar el pivote 
        left = [x for x in arr if x < pivot]  # elementos menores al pivote
        middle = [x for x in arr if x == pivot]  # elementos iguales al pivote
        right = [x for x in arr if x > pivot]  # elementos mayores al pivote
        return quick_sort(left) + middle + quick_sort(right)

# funcion para medir tiempo de ejecucion
def measure_quick_sort():
    input_sizes = [10, 100, 1000, 5000, 10000, 20000, 1000000]  # Tamaños de array, incluyendo uno grande
    for size in input_sizes:
        # Generar array aleatorio para probar
        test_array = [random.randint(0, 100000) for _ in range(size)]
        start_time = time.time()
        quick_sort(test_array.copy())
        end_time = time.time()
        time_taken = end_time - start_time
        print(f"Array Size: {size}, Time Taken: {time_taken:.6f} seconds")

# Ejecutar la función de medición de tiempo
if __name__ == "__main__":
    measure_quick_sort()
