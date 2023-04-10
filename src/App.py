import random
import time
import matplotlib.pyplot as plt

# Implementation of the three sorting algorithms
def heap_sort(arr):
    def heapify(arr, n, i):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < n and arr[left] > arr[largest]:
            largest = left

        if right < n and arr[right] > arr[largest]:
            largest = right

        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            heapify(arr, n, largest)

    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

    return arr

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    i = j = 0
    merged = []
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    merged += left[i:]
    merged += right[j:]

    return merged

def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)

# Generate random arrays of various sizes
array_sizes = [10**2, 10**3, 10**4]
arrays = [[random.randint(1, 10**6) for _ in range(size)] for size in array_sizes]

# Time each sorting algorithm on each array
times = []
for arr in arrays:
    heap_start = time.time()
    heap_sort(arr)
    heap_end = time.time()

    merge_start = time.time()
    merge_sort(arr)
    merge_end = time.time()

    quick_start = time.time()
    quick_sort(arr)
    quick_end = time.time()

    times.append([heap_end - heap_start, merge_end - merge_start, quick_end - quick_start])

# Create a graph comparing the three algorithms
plt.plot(array_sizes, [time[0] for time in times], label='Heap Sort')
plt.plot(array_sizes, [time[1] for time in times], label='Merge Sort')
plt.plot(array_sizes, [time[2] for time in times], label='Quick Sort')
plt.xscale('log')
plt.xlabel('Array Size (log scale)')
plt.ylabel('Time (seconds)')
plt.legend()
plt.show()
