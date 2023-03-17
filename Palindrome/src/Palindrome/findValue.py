def find_value(arr, val):
    """This function returns the index of the first occurrence of val in arr,
    or -1 if val is not in arr."""
    for i in range(len(arr)):
        if arr[i] == val:
            return i
    return -1
