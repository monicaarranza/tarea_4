import time
import random


def merge_sort(arr):
    if len(arr) > 1:
        # encontrar el punto medio del array
        mid = len(arr) // 2
        # dividir el array en dos mitades
        left_half = arr[:mid]
        right_half = arr[mid:]

        # ordenar recursivamente ambas mitades
        merge_sort(left_half)
        merge_sort(right_half)

        # mergear las dos mitades
        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        # copiar los elementos restantes
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

    return arr

# funcion para medir tiempo de ejecucion
def measure_merge_sort():
    input_sizes = [10, 100, 1000, 5000, 10000, 20000, 1000000]  # tamaños de array
    for size in input_sizes:
        # generar array aleatorio para probar
        test_array = [random.randint(0, 100000) for _ in range(size)]
        start_time = time.time()
        merge_sort(test_array.copy())
        end_time = time.time()
        time_taken = end_time - start_time
        print(f"Array Size: {size}, Time Taken: {time_taken:.6f} seconds")

# ejecutar la funcion de tiempo
if __name__ == "__main__":
    measure_merge_sort()
