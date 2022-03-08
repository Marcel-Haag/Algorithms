def fibonacciSearch(list, target):
    size = len(list)

    start = -1

    f0 = 0
    f1 = 1
    f2 = 1
    while f2 < size:
        f0 = f1
        f1 = f2
        f2 = f1 + f0

    while f2 > 1:
        index = min(start + f0, size - 1)
        if list[index] < target:
            f2 = f1
            f1 = f0
            f0 = f2 - f1
            start = index
        elif list[index] > target:
            f2 = f0
            f1 = f1 - f0
            f0 = f2 - f1
        else:
            return index
    if f1 and (list[size - 1] == target):
        return size - 1
    return None


list = [2, 4, 8, 11, 13, 17, 18, 19, 21, 23, 27]
e = 4
print(fibonacciSearch(list, e))
