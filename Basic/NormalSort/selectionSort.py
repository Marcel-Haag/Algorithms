def selectionSort(list: []):
    i = 0
    while i < len(list):
        min = i
        j = i + 1
        print("Ahead of the " + str((i + 1)) + ". run through is the list still " + str(list))

        while j < len(list):
            if list[j] < list[min]: min = j
            j += 1
        temp = list[i]
        list[i] = list[min]
        list[min] = temp
        i += 1
    return list


list = [1, 7, 234, 23, 44, 5]
print("The list " + str(list) + " can be sorted using SelectionSort to " + str(selectionSort(list)))
