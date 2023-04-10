
def mergeSort(list_to_sort):
    """
    Sorts the given list using merge sort algorithm

    Parameters
    ----------
        list_to_sort : list
            List for sorting
    Returns
    ----------
        list : list
            A new list containing the elements of list_to_sort, sorted
    """
    if len(list_to_sort) <= 1:
        return list_to_sort

    mid = len(list_to_sort) // 2
    left_half = list_to_sort[:mid]
    right_half = list_to_sort[mid:]

    left_half = mergeSort(left_half)
    right_half = mergeSort(right_half)

    return merge(left_half, right_half)


def merge(left_half, right_half):
    """
    Merges two sorted lists into one sorted list

    Parameters
    ----------
        left_half : list
            First sorted list to merge
        right_half : list
            Second sorted list to merge
    Returns
    ----------
        list : list
            A new list containing the elements of left_half and right_half, sorted
    """
    merged = []

    left_index, right_index = 0, 0
    while left_index < len(left_half) and right_index < len(right_half):
        if left_half[left_index] < right_half[right_index]:
            merged.append(left_half[left_index])
            left_index += 1
        else:
            merged.append(right_half[right_index])
            right_index += 1

    merged += left_half[left_index:]
    merged += right_half[right_index:]

    return merged
if __name__ == "__main__":
    print(mergeSort([122, 4445, 21312, 112321, 4434, 711, 71, 2221, 332, 7300, 344, 223, 24, 26, 112, 55, 1, 0]))
