def heapify(list: [], n: int, i: int):
    largestRoot = i
    left = 2 * i + 1
    right = 2 * i + 2

    # See if left child of root exists and is greater than root
    if left < n and list[largestRoot] < list[left]:
        largestRoot = left

    # See if right child of root exists and is greater than root
    if right < n and list[largestRoot] < list[right]:
        largestRoot = right

    # Change root, if needed
    if largestRoot != i:
        list[i], list[largestRoot] = list[largestRoot], list[i]  # make swap
        # Heapify the root.
        heapify(list, n, largestRoot)


def heapSort(list: []):
    n = len(list)

    # Build a maxheap.
    for i in range(n // 2 - 1, -1, -1):
        heapify(list, n, i)

    # Extract elements
    for i in range(n - 1, 0, -1):
        list[i], list[0] = list[0], list[i]  # make swap
        heapify(list, i, 0)
    return list


list = [1, 7, 234, 23, 44, 5]
print(str(heapSort(list)))
