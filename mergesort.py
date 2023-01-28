import numpy as np

DEBUG = True


def merge_sort(arr):

    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_arr = arr[:mid]
    right_arr = arr[mid:]

    left_arr = merge_sort(left_arr)
    right_arr = merge_sort(right_arr)

    return merge(left_arr, right_arr)


def merge(left, right):

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
        print('your sorted array: ')
        print(merge_sort(np.array(arr)))


if __name__ == '__main__':
    main()
