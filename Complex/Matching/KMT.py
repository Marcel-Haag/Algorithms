import math


def next(j: int):
    if j == 0: return 0
    if j == 1: return 1
    if j == 2: return 0
    if j == 3: return 1
    if j == 4: return 3
    if j == 5: return 0
    if j == 6: return 2
    if j == 7: return 2
    return 0


def matchingKMT(scanInput: int, pattern: int):
    si = 0
    pi = 0
    # Note: int(math.log10(integer)) + 1 return the number of digits of an integer
    while (si < int(math.log10(scanInput)) + 1) and (pi < int(math.log10(pattern)) + 1):
        if str(pattern)[pi] == str(scanInput)[si]:
            if pi == (int(math.log10(pattern))): return True
            pi += 1
        else:
            pi = next(pi)
        si += 1
    return False


scanInput = 10101010010
pattern = 101001

print(str(matchingKMT(scanInput, pattern)))
