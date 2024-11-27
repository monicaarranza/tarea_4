import time
import random


def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        # mover elementos mayores al key una posicion adelante
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

# funcion para medir tamano de array y tiempo de ejecucion
def measure_insertion_sort():
    input_sizes = [10, 100, 1000, 5000, 10000, 20000]  # tamanos de array
    for size in input_sizes:
        # generar array tandom para probar
        test_array = [random.randint(0, 100000) for _ in range(size)]
        start_time = time.time()  
        insertion_sort(test_array.copy())  
        end_time = time.time()  
        time_taken = end_time - start_time
        print(f"Array Size: {size}, Time Taken: {time_taken:.6f} seconds")

# ejecutar funcion de tiempo
if __name__ == "__main__":
    measure_insertion_sort()
