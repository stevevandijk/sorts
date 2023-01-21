import numpy as np

DEBUG = True


def heap_sort(arr) -> list:
    quantity = len(arr)

    # Hier wordt achteruit gelooped door de elementen van de lijst, waarbij ini_parent de parent_idx wordt.
    # Als het heapify proces is gedaan, staat het grootste element aan het begin van de array.
    # (Het heapify proces zet een array om in zijn max-heap data-structuur)

    for ini_parent in range(quantity, -1, -1):
        heapify(arr, quantity, ini_parent)

    # Nu de array is zijn max-heap staat wordt het eerste grootste element omgewisseld met het laatste element uit
    # de array.
    # Vervolgens wordt heapify weer aangeroepen, die vervolgens voor de overige ongesorteerde elementen
    # hetzelfde proces herhaalt.
    # Als dat is gedaan wordt het nogmaals herhaalt, totdat deze for loop alles heeft gesorteerd.

    for idx in range(quantity - 1, 0, -1):
        arr[idx], arr[0] = arr[0], arr[idx]
        heapify(arr, idx, 0)

    # print('Your sorted list:')
    print(arr)
    return arr


def heapify(arr: list, quantity: int, ini_parent: int) -> None:

    # Parent is de index van de parent-node, left_idx is de index van de left child-node en right_idx
    # is de index van right child_node.

    parent_idx = ini_parent
    left_idx = 2 * ini_parent + 1
    right_idx = 2 * ini_parent + 2

    # Hier wordt gecheckt of de left child-node groter is dan de parent-node.
    # Zo ja dan wordt de nieuwe parent index, de index van de left child-node.
    # Ook wordt er gechekt of de index van de left child-node kleiner dan de hoogst mogelijk indexgetal van
    # de array, namelijk quantity.

    if left_idx < quantity and arr[ini_parent] < arr[left_idx]:
        parent_idx = left_idx

    # Dezelfde check wordt gedaan voor de right child-node. Echter kan het nu zo zijn dat de left child-node de
    # nieuwe parent-node is geworden, dus daarom arr[parent] in plaats van arr[index].

    if right_idx < quantity and arr[parent_idx] < arr[right_idx]:
        parent_idx = right_idx

    # Hier wordt er gecheckt of de parent-node is veranderd.
    # Als dat zo is wordt de nieuwe parent-node, de rechter of de linker child-node afhankelijk van welke
    # de nieuwe parent-node is geworden.
    # Daarna roept de functie zichzelf weer aan, maar is de nieuwe ini_parent, parent_idx.

    if parent_idx != ini_parent:
        arr[ini_parent], arr[parent_idx] = arr[parent_idx], arr[ini_parent]
        heapify(arr, quantity, parent_idx)


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
    input_arr = input('input your list: ')
    arr = validate_input(input_arr)
    heap_sort(np.array(arr))


if __name__ == '__main__':
    main()
