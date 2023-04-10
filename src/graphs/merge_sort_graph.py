import random
import time
import matplotlib.pyplot as plt
from src.sorting.merge import mergeSort

def plot_merge_sort(arr):
    fig, ax = plt.subplots()

    # Set the x and y limits of the plot
    ax.set_xlim(0, len(arr))
    ax.set_ylim(0, max(arr))

    # Set the title and labels
    ax.set_title('Merge Sort')
    ax.set_xlabel('Index')
    ax.set_ylabel('Value')

    # Plot the initial array
    rects = ax.bar(range(len(arr)), arr)

    # Sort the array and plot each step
    sorted_arr = mergeSort(arr)
    for i in range(len(sorted_arr)):
        for j in range(len(arr)):
            if arr[j] == sorted_arr[i]:
                arr[i], arr[j] = arr[j], arr[i]
                for k in range(len(arr)):
                    rects[k].set_height(arr[k])
                plt.pause(0.001)
                plt.draw()

    plt.show()


if __name__ == "__main__":
    arr = [random.randint(1, 100) for i in range(20)]
    plot_merge_sort(arr)
