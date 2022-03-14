def minSearch(list: []):
    min = list[0]
    for i in range(0, len(list) - 1):
        if list[i] < list[min]: min = i
    return list[min]


list = [1, 5, 7, 23, 44, 234]
print("Smallest element of list " + str(list) + " is: " + str(minSearch(list)))
