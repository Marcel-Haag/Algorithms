def maxSearch(list: []):
    max = list[0]
    for i in range(0, len(list) - 1):
        if list[i] > list[max]: max = i
    return list[max]


list = [1, 5, 7, 23, 44, 234]
print("Biggest element of list " + str(list) + " is: " + str(maxSearch(list)))
