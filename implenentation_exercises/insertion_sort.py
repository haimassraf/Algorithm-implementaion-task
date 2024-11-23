import random


def insertion_sort(arr):
    comparisons = initializations = 0
    for j in range(1, len(arr)):
        key = arr[j]
        i = j - 1
        comparisons += 1
        while i >= 0 and arr[i] > key:
            comparisons += 1
            arr[i + 1] = arr[i]
            i -= 1
            initializations += 1
        arr[i + 1] = key
        initializations += 1
    return comparisons, initializations


my_list = [random.randint(-50, 50) for _ in range(20)]
print(insertion_sort(my_list))
print(my_list)
