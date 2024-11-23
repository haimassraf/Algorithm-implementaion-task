import random


def partition(arr, p, r):
    comparisons = initializations = 0
    random_index = random.randint(p, r)
    initializations += 2
    arr[r], arr[random_index] = arr[random_index], arr[r]
    x = arr[r]
    j = p - 1
    for i in range(p, r):
        comparisons += 1
        if arr[i] <= x:
            j += 1
            initializations += 2
            arr[i], arr[j] = arr[j], arr[i]
    initializations += 2
    arr[j + 1], arr[r] = arr[r], arr[j + 1]
    return j + 1, comparisons, initializations


def __quick_sort(arr, p, r):
    comparisons = initialization = 0
    if p < r:
        q, c, i = partition(arr, p, r)
        left_comparison, left_initialization = __quick_sort(arr, p, q - 1)
        right_comparison, right_initialization = __quick_sort(arr, q + 1, r)
        comparisons = c + left_comparison + right_comparison
        initialization = i + left_comparison + right_comparison
    return comparisons, initialization


def quick_sort(arr):
    return __quick_sort(arr, 0, len(arr) - 1)


my_list = [random.randint(-50, 50) for _ in range(20)]
print(quick_sort(my_list))
print(my_list)
