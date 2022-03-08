def binarySearch(element: int, numbers: []):
    low = 0
    last = len(numbers) - 1
    while low <= last:
        middle = int((low + last) / 2)
        print("I test the area " + str(low) + " to " + str(last) + " with Pivot = " + str(middle))

        if numbers[middle] < element:
            low = middle + 1
        else:
            if numbers[middle] == element:
                return True
            else:
                last = middle - 1
    return False


list = [1, 5, 7, 23, 44, 234]
e = 44
if binarySearch(e, list):
    print("The element " + str(e) + " is in the array " + str(list))
else:
    print("The element " + str(e) + " is not in the array " + str(list))
