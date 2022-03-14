def quickSort(list: []):
    if len(list) <= 1: return list
    # Finding the pivot of the list
    # Note: Doesn't have to be the median
    pivot = len(list) // 2

    L = []
    R = []
    index = 0

    for element in list:
        if index != pivot and element <= list[pivot]:
            L.append(element)
        if index != pivot and element > list[pivot]:
            R.append(element)
        index += 1

    sortedList = []
    sortedList.extend(quickSort(L))
    sortedList.append(list[pivot])
    sortedList.extend(quickSort(R))

    return sortedList


list = [1, 7, 234, 23, 44, 5]
print(str(quickSort(list)))
