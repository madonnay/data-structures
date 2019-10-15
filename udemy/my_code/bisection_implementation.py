def bisection_iter(target, array):
    start = 0
    stop = len(array) - 1
    while start <= stop:
        mid = (start + stop) // 2
        if target == array[mid]:
            return mid, f"{target} found at index {mid}"
        elif target < array[mid]:
            stop = mid - 1
        else:
            start = mid + 1
    return None, f"{target} not found in list"
