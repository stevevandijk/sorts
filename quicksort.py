import random

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
        left = quicksort(left)
        right = quicksort(right)
        for i in right:
            left.append(i)
        return left

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
