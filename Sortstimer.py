import re
from copy import copy
from timeit import default_timer as timer
import numpy as np

DEBUG = True

"""This is the sorts timer. It's a class with all the sorts and a timer function to time how long it takes for the sorting algorithms to sort the list
the user inputs!"""

# This function is used to time the algorithms


def timed(func):
    def wrapper_function(*args, **kwargs):
        start = timer()
        func(*args, **kwargs)
        print("Timed:", (timer() - start) * 1000, "ms")

    return wrapper_function

# If the list that is being input is too long for display, this method shrinks the list in the following way
# [1, 2, 3, 4, ... , 97, 98, 99, 100]


def list_for_printing(arr):
    if len(arr) > 20:
        left = arr[0:4]
        right = arr[-4:]

        ret = "["
        for i in left:
            ret += "%s, " % i
        ret += "... "
        for i in right:
            ret += ", %s" % i
        ret += "]"
        return ret
    return arr


class Sorts(object):
    def __init__(self, arr) -> None:
        self.arr = copy(arr)
        self.orig_arr: list = copy(arr)
        self.qs_lower: int = 0
        self.qs_upper: int = len(self.arr) - 1

    def __repr__(self) -> str:
        return "Sorts[\n   original: %s,\n     sorted: %s\n]" % (
            list_for_printing(self.orig_arr), list_for_printing(self.arr))

    # resets the input list to its original input
    def reset(self) -> None:
        self.arr = copy(self.orig_arr)

    def __quick_sort(self, lower: int, upper: int) -> None:

        def partition(p_lower: int, p_upper: int) -> int:
            pivot = self.arr[p_upper]
            n = p_lower - 1

            for k in range(p_lower, p_upper):
                if self.arr[k] <= pivot:
                    n += 1
                    self.arr[n], self.arr[k] = self.arr[k], self.arr[n]

            self.arr[n + 1], self.arr[p_upper] = self.arr[p_upper], self.arr[n + 1]

            return n + 1

        if lower < upper:
            pivot_num = partition(lower, upper)
            self.__quick_sort(lower, pivot_num - 1)
            self.__quick_sort(pivot_num + 1, upper)

    def __merge_sort(self, arr: list) -> list:

        def merge(left: list, right: list) -> list:
            sorted_arr = []
            left_idx, right_idx = 0, 0
            length_left, length_right = len(left), len(right)

            while left_idx < length_left and right_idx < length_right:
                if left[left_idx] <= right[right_idx]:
                    sorted_arr.append(left[left_idx])
                    left_idx += 1
                else:
                    sorted_arr.append(right[right_idx])
                    right_idx += 1

            while left_idx < length_left:
                sorted_arr.append(left[left_idx])
                left_idx += 1

            while right_idx < length_right:
                sorted_arr.append(right[right_idx])
                right_idx += 1

            return sorted_arr

        if len(arr) <= 1:
            return arr

        mid = len(arr) // 2
        left_arr = arr[:mid]
        right_arr = arr[mid:]
        left_arr = self.__merge_sort(left_arr)
        right_arr = self.__merge_sort(right_arr)

        return merge(left_arr, right_arr)

    @timed
    def heap_sort(self) -> None:

        def heapify(arr: list, h_quantity: int, h_ini_parent: int) -> None:
            parent_idx = h_ini_parent
            left_idx = 2 * h_ini_parent + 1
            right_idx = 2 * h_ini_parent + 2

            if left_idx < h_quantity and arr[h_ini_parent] < arr[left_idx]:
                parent_idx = left_idx

            if right_idx < h_quantity and arr[parent_idx] < arr[right_idx]:
                parent_idx = right_idx

            if parent_idx != h_ini_parent:
                arr[h_ini_parent], arr[parent_idx] = arr[parent_idx], arr[h_ini_parent]
                heapify(arr, h_quantity, parent_idx)

        quantity = len(self.arr)

        for ini_parent in range(quantity, -1, -1):
            heapify(self.arr, quantity, ini_parent)

        for idx in range(quantity - 1, 0, -1):
            self.arr[idx], self.arr[0] = self.arr[0], self.arr[idx]
            heapify(self.arr, idx, 0)

    @timed
    def quick_sort(self) -> None:
        self.__quick_sort(self.qs_lower, self.qs_upper)

    @timed
    def merge_sort(self) -> None:
        self.arr = self.__merge_sort(self.arr)

    @timed
    def insertion_sort(self) -> None:
        quantity = len(self.arr)

        for idx in range(1, quantity):
            predecessor_idx = idx - 1
            key = self.arr[idx]

            while predecessor_idx >= 0 and key < self.arr[predecessor_idx]:
                self.arr[predecessor_idx + 1] = self.arr[predecessor_idx]
                predecessor_idx -= 1

            self.arr[predecessor_idx + 1] = key


def validate_input(value: str) -> list:
    items = re.split(r"[,\s]+", value)
    ret = []
    for item in items:
        try:
            ret.append(int(item))
        except ValueError:
            if DEBUG:
                print("Invalid value [{}] ignoring...".format(item))
    return ret


def main() -> None:
    while True:
        input_arr = input('input your list, separate the elements of the list with spaces, commas or: ')
        if input_arr == 'stop':
            break
        arr = validate_input(input_arr)
        sorts_std_list = Sorts(arr)
        sorts_np_list = Sorts(np.array(arr))
        print("Heap sort")
        sorts_std_list.heap_sort()
        print(sorts_std_list)
        print("Heap sort - np")
        sorts_np_list.heap_sort()
        print(sorts_np_list)

        print("Quick sort")
        sorts_std_list.reset()
        sorts_std_list.quick_sort()
        print(sorts_std_list)
        print("Quick sort - np")
        sorts_np_list.reset()
        sorts_np_list.quick_sort()
        print(sorts_np_list)

        print("Merge sort")
        sorts_std_list.reset()
        sorts_std_list.merge_sort()
        print(sorts_std_list)
        print("Merge sort - np")
        sorts_np_list.reset()
        sorts_np_list.merge_sort()
        print(sorts_np_list)

        print("Insertion sort")
        sorts_std_list.reset()
        sorts_std_list.insertion_sort()
        print(sorts_std_list)
        print("Insertion sort - np")
        sorts_np_list.reset()
        sorts_np_list.insertion_sort()
        print(sorts_np_list)


if __name__ == '__main__':
    main()
