def FindIndexRotation(array):
    return FindIndexRotation1(array, 0, len(array) -1)


def FindIndexRotation1(alist, low, high):
    mid = (low + high ) // 2
    if mid == 0 or mid == len(alist) - 1:
        return mid

    if alist[mid - 1] > alist[mid] and alist[mid + 1] >= alist[mid]:
        return mid
    elif alist[mid] > alist[high]:
        return FindIndexRotation1(alist, mid, high)
    else:
        return FindIndexRotation1(alist, low, mid)

print FindIndexRotation([3,3,3,3,1,2])
