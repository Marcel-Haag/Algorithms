def linearSearch(element: int, numbers: []):
    i = 0
    while i < len(numbers):
        if numbers[i] == element:
            return True
        i = i + 1
    return False


list = [1, 5, 7, 23, 44, 234]
e = 44
if linearSearch(e, list):
    print("The element " + str(e) + " is in the array " + str(list))
else:
    print("The element " + str(e) + " is not in the array " + str(list))
