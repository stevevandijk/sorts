import numpy as np

DEBUG = True


def quicksort(arr, lower, upper):

    if lower < upper:

        # We find the pivot element such that
        # the element smaller than the pivot element are on the left and
        # the element greater than the pivot element are on the right

        pivot_num = partition(arr, lower, upper)

        # Here quicksort calls itself on the left of the pivot

        quicksort(arr, lower, pivot_num - 1)

        # Here quicksort calls itself on the right of the pivot

        quicksort(arr, pivot_num + 1, upper)

    return arr


def partition(arr, lower, upper):

    # Here you choose the pivot element to be the rightmost element.

    pivot = arr[upper]

    # Pointer for the greater element

    n = lower - 1

    # Here we compare all elements with the pivot element

    for k in range(lower, upper):
        if arr[k] <= pivot:

            # If an element is smaller or equal to the pivot element
            # it gets swapped with the greater element pointed to by n

            n += 1

            # So that mean the k-th element gets swapped with the n-th element

            arr[n], arr[k] = arr[k], arr[n]

    # Here we swap the pivot element with the greater element pointed to by n

    arr[n + 1], arr[upper] = arr[upper], arr[n + 1]

    # And lastly return the position form where the separation is done

    return n + 1


def validate_input(value: str) -> list:
    items = value.split(' ')
    ret = []
    for item in items:
        try:
            ret.append(int(item))
        except ValueError:
            if DEBUG:
                print("Invalid value [{}] ignoring...".format(item))
    return ret


def main():
    while True:
        input_arr = input('input your list, separate the elements of the list with spaces: ')
        if input_arr == 'stop':
            break
        arr = validate_input(input_arr)
        print('your sorted list: ')
        print(quicksort(np.array(arr), 0, len(arr) - 1))


if __name__ == '__main__':
    quicksort([8, 3, 4, 2, 5], 0, 4)
    main()
