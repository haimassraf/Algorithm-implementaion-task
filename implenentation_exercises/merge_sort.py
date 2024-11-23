import random


def merge(arr, start, mid, end):
    comparisons = initializations = 0
    left = arr[start: mid + 1]
    right = arr[mid + 1: end + 1]
    i = j = 0
    k = start

    comparisons += 1
    while i < len(left) and j < len(right):
        comparisons += 1
        if left[i] < right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1
        initializations += 1

    while i < len(left):
        arr[k] = left[i]
        initializations += 1
        i += 1
        k += 1
    return comparisons, initializations


def __merge_sort(arr, start, end):
    comparisons = initializations = 0
    if start < end:
        mid = (start + end) // 2
        c1, i1 = __merge_sort(arr, start, mid)
        c2, i2 = __merge_sort(arr, mid + 1, end)
        c3, i3 = merge(arr, start, mid, end)
        comparisons += c1 + c2 + c3
        initializations += i1 + i2 + i3

    return comparisons, initializations


def merge_sort(arr):
    c, i = __merge_sort(arr, 0, len(arr))
    return c, i


my_list = [random.randint(-50, 50) for _ in range(20)]
print(merge_sort(my_list))
print(my_list)
