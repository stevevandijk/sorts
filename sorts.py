import random
def heapsort(a):

    return 

def quicksort(k):
    if order(k) == 0:
        return k
    else:
        b = len(k)
        c = random.randrange(0,b)
        d = k[c]
        left = []
        right = []
        for i in k:
            if i > d:
                right.append(i)
            else:
                left.append(i)
        for i in right:
            left.append(i)
        left = quicksort(left)
        return left
def insertionsort(k):
    control = order(k)
    place = 0
    maxplace = len(k) -1
    while control == 1:
        place2 = place +1
        left = k[place]
        right = k[place2]
        if left > right:
            k[place] = right
            k[place2] = left
        place = place + 1
        if place == maxplace:
            place = 0
        control = order(k)
    return k
def order(test_list):
    temp = 0
    i = 1
    while i < len(test_list):
        if(test_list[i] < test_list[i - 1]):
            temp = 1
        i += 1
    if (temp == 0) :
        return temp
    else :
        return temp
