import time
import random

def selection_sort(arr):
    for i in range(len(arr)):
        # indice de menor valor en el array no ordenado
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        # cambiar el valor minimo con el primer valor del array no ordenado
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

# funcion medir tiempo de ejecucion
def measure_selection_sort():
    input_sizes = [10, 100, 1000, 5000, 10000, 20000]  # sizes de array
    for size in input_sizes:
        # generar array aleatorio para probar
        test_array = [random.randint(0, 100000) for _ in range(size)]
        start_time = time.time()
        selection_sort(test_array.copy())
        end_time = time.time()
        time_taken = end_time - start_time
        print(f"Array Size: {size}, Time Taken: {time_taken:.6f} seconds")

# ejecutar la funcion de tiempo
if __name__ == "__main__":
    measure_selection_sort()
