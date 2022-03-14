def mergeSort(list: []):
    if len(list) <= 1: return list

    pivot = len(list) // 2
    L = list[:pivot]
    R = list[pivot:]

    mergeSort(L)
    mergeSort(R)

    i = j = k = 0

    while i < len(L) and j < len(R):
        if L[i] < R[j]:
            list[k] = L[i]
            i += 1
        else:
            list[k] = R[j]
            j += 1
        k += 1

    while i < len(L):
        list[k] = L[i]
        i += 1
        k += 1

    while j < len(R):
        list[k] = R[j]
        j += 1
        k += 1

    return list


# radixSort for postal codes
def radixSortForPostalCodes(list: []):
    Box0 = []
    Box1 = []
    Box2 = []
    Box3 = []
    Box4 = []
    Box5 = []
    Box6 = []
    Box7 = []
    Box8 = []
    Box9 = []

    for e in list:
        firstDigit = int(e / 10000)
        if firstDigit == 0: Box0.append(e)
        if firstDigit == 1: Box1.append(e)
        if firstDigit == 2: Box2.append(e)
        if firstDigit == 3: Box3.append(e)
        if firstDigit == 4: Box4.append(e)
        if firstDigit == 5: Box5.append(e)
        if firstDigit == 6: Box6.append(e)
        if firstDigit == 7: Box7.append(e)
        if firstDigit == 8: Box8.append(e)
        if firstDigit == 9: Box9.append(e)

    result = []
    result.extend(mergeSort(Box0))
    result.extend(mergeSort(Box1))
    result.extend(mergeSort(Box2))
    result.extend(mergeSort(Box3))
    result.extend(mergeSort(Box4))
    result.extend(mergeSort(Box5))
    result.extend(mergeSort(Box6))
    result.extend(mergeSort(Box7))
    result.extend(mergeSort(Box8))
    result.extend(mergeSort(Box9))

    return result


# radixSort for names
def radixSortForNames(list: []):
    LetterBoxA = []
    LetterBoxL = []
    LetterBoxM = []
    LetterBoxN = []
    LetterBoxP = []
    LetterBoxS = []

    for e in list:
        firstChar = str(e[0])
        if firstChar == 'A': LetterBoxA.append(e)
        if firstChar == 'L': LetterBoxL.append(e)
        if firstChar == 'M': LetterBoxM.append(e)
        if firstChar == 'N': LetterBoxN.append(e)
        if firstChar == 'P': LetterBoxP.append(e)
        if firstChar == 'S': LetterBoxS.append(e)

    result = []
    result.extend(mergeSort(LetterBoxA))
    result.extend(mergeSort(LetterBoxL))
    result.extend(mergeSort(LetterBoxM))
    result.extend(mergeSort(LetterBoxN))
    result.extend(mergeSort(LetterBoxP))
    result.extend(mergeSort(LetterBoxS))

    return result


postalCodes = [4315, 22345, 11111, 4312, 55423, 88768, 12222]
print(str(radixSortForPostalCodes(postalCodes)))
names = ['Meier', 'Lehmann', 'Schulze', 'Maskowski', 'Peters', 'Albert', 'Maler', 'Nietschke', 'Meiner', 'Asse']
print(str(radixSortForNames(names)))