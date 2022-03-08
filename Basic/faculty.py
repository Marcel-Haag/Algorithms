def fakulty(number: int):
    factor = 1
    nFaculty = 1
    while True:
        print("I have calculated: n = " + str(number) + " factor = " + str(factor) + " nFaculty = " + str(nFaculty))
        if number <= factor:
            return nFaculty
        factor = factor + 1
        nFaculty = nFaculty * factor


n = 5
# 0! = 1
# n! = 1 * 2 * 3 * ... * (n – 1) * n
print("fakulty(" + str(n) + ") = " + str(fakulty(n)))
