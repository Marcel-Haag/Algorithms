def mixMaxSearch(list: []):
    min = list[0]
    max = list[0]
    for element in list:
        if element > max: max = element
        if element < min: min = element
    result = []
    result.append(max)
    result.append(min)
    return result


list = [1, 5, 7, 23, 44, 234]
print("Biggest and smallest element of list " + str(list) + " are: " + str(mixMaxSearch(list)))
