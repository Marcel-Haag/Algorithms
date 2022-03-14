def matchingBruteForce(scanInput: str, pattern: str):
    found = False
    for si in range(0, (len(scanInput) - len(pattern))):
        nrMatched = 0
        for pi in range(0, (len(pattern))):
            if pattern[pi] == scanInput[si + pi]:
                nrMatched += 1
        if nrMatched == len(pattern):
            found = True
    return found


scanInput = "All Algorithms are cool."
pattern = "cool"

print(str(matchingBruteForce(scanInput, pattern)))
