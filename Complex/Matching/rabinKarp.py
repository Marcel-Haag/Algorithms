import math


def hash(x):
    return int(x) % 11


def matchingBruteForce(scanInput: int, pattern: int):
    found = False
    for si in range(0, (int(math.log10(scanInput)) + 1 - int(math.log10(pattern)) + 1)):
        nrMatched = 0
        for pi in range(0, (int(math.log10(pattern)))):
            if str(pattern)[pi] == str(scanInput)[si + pi]:
                nrMatched += 1
        if nrMatched == (int(math.log10(pattern))):
            found = True
    return found


def matchingRabinKarp(scanInput: int, pattern: int):
    found = False
    patternHash = hash(pattern)
    # Note: int(math.log10(integer)) + 1 return the number of digits of an integer
    for si in range(0, ((int(math.log10(scanInput)) + 1) - (int(math.log10(pattern)) + 1))):
        temp = str(scanInput)[si:(si + (int(math.log10(pattern)) + 1))]
        scanHash = hash(temp)
        if patternHash == scanHash:
            if matchingBruteForce(pattern, int(temp)): found = True
    return found


scanInput = 852367384194
pattern = 841

print(str(matchingRabinKarp(scanInput, pattern)))
