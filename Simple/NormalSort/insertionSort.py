def insertionSort(list: []):
    for i in range(1, len(list)):
        key = list[i]
        j = i - 1

        while j >= 0 and key < list[j]:
            list[j + 1] = list[j]
            j -= 1

        list[j + 1] = key
    return list


list = [1, 7, 234, 23, 44, 5]
print("The list " + str(list) + " can be sorted using InsertionSort to " + str(insertionSort(list)))
