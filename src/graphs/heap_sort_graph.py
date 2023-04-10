import random
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from src.sorting.heap import heapSort
def plot_heap_sort(arr):
    fig, ax = plt.subplots()

    # Set the x and y limits of the plot
    ax.set_xlim(0, len(arr))
    ax.set_ylim(0, max(arr))

    # Set the title and labels
    ax.set_title('Heapsort')
    ax.set_xlabel('Index')
    ax.set_ylabel('Value')

    # Plot the initial array
    rects = ax.bar(range(len(arr)), arr)

    # Sort the array and plot each step
    def update(frame):
        nonlocal arr, rects
        heapSort(arr)
        for i in range(len(arr)):
            rects[i].set_height(arr[i])
        return rects,

    ani = FuncAnimation(fig, update, frames=range(len(arr)), repeat=False)

    plt.show()

if __name__ == "__main__":
    arr = [random.randint(1, 100) for i in range(20)]
    plot_heap_sort(arr)
