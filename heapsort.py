import numpy as np


def heap_sort(arr):
    n = len(arr)
    '''Hier wordt de zogenaamde max heap opgebouwd doormiddel van de heapify method'''
    for i in range(n, -1, -1):
        heapify(arr, n, i)
    '''Hier wordt er per element bekeken of die moet worden geswapped'''
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]   # swap
        heapify(arr, i, 0)

    return arr


def heapify(arr, n, i):
    top = i
    left = 2 * i + 1
    right = 2 * i + 2
    if left < n and arr[i] < arr[left]:
        top = left
    if right < n and arr[top] < arr[right]:
        top = right
    if top != i:
        arr[i], arr[top] = arr[top], arr[i]
        heapify(arr, n, top)


array = np.array([8, 9, 3, 2, 1, 3, 7, 8, 10, 11])
print(heap_sort(array))
