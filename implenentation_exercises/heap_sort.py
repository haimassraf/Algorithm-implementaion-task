import random


def heapify(arr, n, i):
    comparisons = initializations = 0
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n:
        comparisons += 1
        if arr[left] > arr[largest]:
            largest = left

    if right < n:
        comparisons += 1
        if arr[right] > arr[largest]:
            largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        initializations += 2
        c, init = heapify(arr, n, largest)
        comparisons += c
        initializations += init

    return comparisons, initializations


def heap_sort(arr):
    comparisons = initializations = 0
    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        c, init = heapify(arr, n, i)
        comparisons += c
        initializations += init

    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        initializations += 2
        c, init = heapify(arr, i, 0)
        comparisons += c
        initializations += init

    return comparisons, initializations


my_list = [random.randint(-50, 50) for _ in range(20)]
print(heap_sort(my_list))
print(my_list)
