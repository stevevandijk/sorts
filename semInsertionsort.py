import numpy as np

DEBUG = True


def insertion_sort(arr):

    quantity = len(arr)

    for idx in range(1, quantity):
        predecessor = idx - 1
        key = arr[idx]

        while predecessor >= 0 and key < arr[predecessor]:
            arr[predecessor + 1] = arr[predecessor]
            predecessor -= 1

        arr[predecessor + 1] = key

    print('your sorted list: ')
    print(arr)
    return arr


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


def main() -> None:
    while True:
        input_arr = input('input your list, separate the elements of the list with spaces: ')
        if input_arr == 'stop':
            break
        arr = validate_input(input_arr)
        insertion_sort(np.array(arr))


if __name__ == '__main__':
    main()
