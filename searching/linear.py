def linear_search(arr, target):
    for i, value in enumerate(arr):
        if value == target:
            return i
    return -1