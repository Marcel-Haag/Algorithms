def quickSelection(list: [], k: int):
    if len(list) <= 1: return list[len(list) - k]
    # Finding the pivot of the list
    # Note: Doesn't have to be the median
    pivot = len(list) // 2
    listOne = []
    listTwo = []
    for element in list:
        index = 0
        if index != pivot and element <= list[pivot]: listOne.append(element)
        if element > list[pivot]: listTwo.append(element)
        index += 1

    if len(listTwo) >= k: return quickSelection(listTwo, k)
    if len(listTwo) + 1 == k: return list[pivot]

    return quickSelection(listOne, k - len(listTwo) - 1)


list = [1, 7, 234, 23, 44, 5]
k = 2
print("The " + str(2) + " element of list " + str(list) + " is: " + str(quickSelection(list, k)))
