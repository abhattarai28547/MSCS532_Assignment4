import time
import random
from heapsort import heapsort

# Helper function to time sorting algorithms
def time_sorting_algorithm(sort_func, arr):
    start_time = time.time()
    sort_func(arr)
    return time.time() - start_time

# Generate random arrays for testing
def generate_test_arrays(size):
    random_arr = [random.randint(1, 100000) for _ in range(size)]
    sorted_arr = sorted(random_arr)
    reverse_sorted_arr = sorted_arr[::-1]
    return random_arr, sorted_arr, reverse_sorted_arr

# Timing for Heapsort, Quicksort, and Merge Sort
def run_sorting_comparisons():
    sizes = [1000, 5000, 10000, 50000, 100000]
    for size in sizes:
        random_arr, sorted_arr, reverse_sorted_arr = generate_test_arrays(size)

        print(f"\nArray size: {size}")
        
        # Heapsort
        heapsort_time = time_sorting_algorithm(heapsort, random_arr.copy())
        print(f"Heapsort (random): {heapsort_time:.5f}s")
        
        # Quicksort (using Python's built-in sorted function for performance comparison)
        quicksort_time = time_sorting_algorithm(sorted, random_arr.copy())
        print(f"Quicksort (random): {quicksort_time:.5f}s")
        
        # Merge Sort (using Python's built-in sorted function)
        mergesort_time = time_sorting_algorithm(sorted, random_arr.copy())
        print(f"Merge Sort (random): {mergesort_time:.5f}s")

         # Heapsort
        heapsort_time = time_sorting_algorithm(heapsort, sorted_arr.copy())
        print(f"Heapsort (sorted): {heapsort_time:.5f}s")
        
        # Quicksort (using Python's built-in sorted function for performance comparison)
        quicksort_time = time_sorting_algorithm(sorted, sorted_arr.copy())
        print(f"Quicksort (sorted): {quicksort_time:.5f}s")
        
        # Merge Sort (using Python's built-in sorted function)
        mergesort_time = time_sorting_algorithm(sorted, sorted_arr.copy())
        print(f"Merge Sort (sorted): {mergesort_time:.5f}s")

         # Heapsort
        heapsort_time = time_sorting_algorithm(heapsort, reverse_sorted_arr.copy())
        print(f"Heapsort (reverse): {heapsort_time:.5f}s")
        
        # Quicksort (using Python's built-in sorted function for performance comparison)
        quicksort_time = time_sorting_algorithm(sorted, reverse_sorted_arr.copy())
        print(f"Quicksort (reverse): {quicksort_time:.5f}s")
        
        # Merge Sort (using Python's built-in sorted function)
        mergesort_time = time_sorting_algorithm(sorted, reverse_sorted_arr.copy())
        print(f"Merge Sort (reverse): {mergesort_time:.5f}s")

# Run the sorting algorithm timing
run_sorting_comparisons()