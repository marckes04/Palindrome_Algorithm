import random
import time
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from  src.sorting.heap import heapSort
from  src.sorting.merge import mergeSort
from  src.sorting.quickSort import quickSort

array_sizes = [0,500,1000,1500,2000,2500,3000,3500,4000,4500,5000]
arrays = [[random.randint(1, 10**6) for _ in range(size)] for size in array_sizes]

# Time each sorting algorithm on each array
times = []
for arr in arrays:
    heap_start = time.time()
    heapSort(arr)
    heap_end = time.time()

    merge_start = time.time()
    mergeSort(arr)
    merge_end = time.time()

    quick_start = time.time()
    quickSort(arr)
    quick_end = time.time()

    times.append([heap_end - heap_start, merge_end - merge_start, quick_end - quick_start])

# Create a graph comparing the three algorithms
fig, ax = plt.subplots()
lines = []
for i in range(3):
    line, = ax.plot([], [], label=['Heap Sort', 'Merge Sort', 'Quick Sort'][i])
    lines.append(line)
ax.set_xlabel('Array Size (log scale)')
ax.set_ylabel('Time (seconds)')
ax.set_xscale('log')
ax.set_xlim(0, 5000)
ax.set_ylim(0, max(max(time) for time in times))

def update(i):
    for j, line in enumerate(lines):
        line.set_data(array_sizes[:i+1], [time[j] for time in times][:i+1])
    return lines

ani = animation.FuncAnimation(fig, update, frames=len(array_sizes), interval=1000, blit=True)
plt.legend()
plt.show()

