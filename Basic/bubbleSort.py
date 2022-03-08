def bubbleSort(list: []):
    i = 0
    while i < len(list):
        print("Ahead of the " + str((i + 1)) + ". run through is the list still " + str(list))
        j = 0
        while j < len(list) - (i + 1):
            if list[j] > list[j + 1]:
                temp = list[j]
                list[j] = list[j + 1]
                list[j + 1] = temp
            j += 1
        i += 1
    return list


list = [1, 7, 234, 23, 44, 5]
print("The list " + str(list) + " can be sorted using BubbleSort to " + str(bubbleSort(list)))
