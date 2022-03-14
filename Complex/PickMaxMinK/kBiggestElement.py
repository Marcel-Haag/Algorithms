def bubbleSort(list: [], k: int):
    i = 0
    while i < k:
        j = 0
        while j < len(list) - (i + 1):
            if list[j] > list[j + 1]:
                temp = list[j]
                list[j] = list[j + 1]
                list[j + 1] = temp
            j += 1
        i += 1
    return list


def selection(list: [], k: int):
    sortedList = bubbleSort(list, k)
    return sortedList[len(sortedList) - k]


list = [1, 7, 234, 23, 44, 5]
k = 2
print("The " + str(2) + " biggest element of list " + str(list) + " is: " + str(selection(list, k)))
