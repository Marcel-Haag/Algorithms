def mergeSort(list: []):
    if len(list) <= 1: return list
    # Finding the pivot of the list
    pivot = len(list) // 2

    # Dividing the array elements
    L = list[:pivot]

    # into 2 halves
    R = list[pivot:]

    print(L)
    print(R)

    # Sorting the first half
    mergeSort(L)

    # Sorting the second half
    mergeSort(R)

    i = j = k = 0

    # Copy data to temp arrays L[] and R[]
    while i < len(L) and j < len(R):
        if L[i] < R[j]:
            list[k] = L[i]
            i += 1
        else:
            list[k] = R[j]
            j += 1
        k += 1

    # Checking if any element was left
    while i < len(L):
        list[k] = L[i]
        i += 1
        k += 1

    while j < len(R):
        list[k] = R[j]
        j += 1
        k += 1

    return list


list = [1, 7, 234, 23, 44, 5]
print(str(mergeSort(list)))
