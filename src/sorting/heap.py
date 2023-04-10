def heapSort(arr):
    """
    Sorts the input list using heapsort algorithm.

    Parameters:
    -----------
    arr: list
        List to be sorted.

    Returns:
    --------
    list
        Sorted list.
    """
    def heapify(arr, n, i):
        """
        Converts the input list into a max heap at given index i.

        Parameters:
        -----------
        arr: list
            List to be heapified.
        n: int
            Number of elements in the list.
        i: int
            Index to start the heapify operation.

        Returns:
        --------
        None
        """
        largest = i  # Initialize largest as root
        left = 2 * i + 1  # left = 2*i + 1
        right = 2 * i + 2  # right = 2*i + 2

        # See if left child of root exists and is greater than root
        if left < n and arr[i] < arr[left]:
            largest = left

        # See if right child of root exists and is greater than root
        if right < n and arr[largest] < arr[right]:
            largest = right

        # Change root, if needed
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]  # Swap

            # Heapify the root.
            heapify(arr, n, largest)

    n = len(arr)

    # Build a maxheap.
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Extract elements one by one
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # Swap
        heapify(arr, i, 0)

    return arr
if __name__ == "__main__":
    print(heapSort([1, 5, 2, 1, 4, 7, 7, 21, 2, 73, 34, 23, -2, 6, 112, -55]))
