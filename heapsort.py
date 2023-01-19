import numpy as np

# Heapsort is een sorteeralgoritme gebaseerd op het onderling vergelijken van de elementen uit de lijst.
# Het algoritme verdeeld de lijst in een ongesorteerde lijst en een gesorteerde lijst.
# Het verkleint de ongesorteerde lijst door telkens het grooste element eruit te halen en die toe te voegen
# aan de gesorteerde lijst.
# Om dit te doen gebruikt heapsort een zogenaamde heap data structuur, in het bijzonder 'max-heap'
# Max-heap is een binary tree dat voldoet aan de eigenschap dat de waarde op elke node groter of gelijk moet zijn
# aan de waarde van zijn child-nodes.
# Om de array om te zetten naar zijn max-heap, ondergaat de array het heapify proces.
# Het heapify proces vergelijkt de nodes met zijn child-nodes en indien er niet wordt voldaan aan de bovengenoemde
# eigenschap, wordt de node omgewisselt met zijn de desbetreffende child-node.
# Dit wordt gedaan totdat er niks meer hoeft worden omgewisselt.
# Vervolgens worden het laatste en het eerste element laatste element van de max-heap omgewisselt en wordt proces
# herhaalt voor alle elementen behalve het laatste gesorteerde (grootste) element aan het einde van de lijst.

def heap_sort(arr):
    n = len(arr)
    # Hier wordt de zogenaamde max-heap opgebouwd doormiddel van de heapify method
    for i in range(n, -1, -1):
        heapify(arr, n, i)
    # Hier wordt er per element bekeken of die moet worden geswapped
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
