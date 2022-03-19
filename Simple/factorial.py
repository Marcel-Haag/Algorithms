def factorial(number: int):
    factor = 1
    nFactorial = 1
    while True:
        print("I have calculated: n = " + str(number) + " factor = " + str(factor) + " nFaculty = " + str(nFactorial))
        if number <= factor:
            return nFactorial
        factor = factor + 1
        nFactorial = nFactorial * factor


n = 5
# 0! = 1
# n! = 1 * 2 * 3 * ... * (n – 1) * n
print("factorial(" + str(n) + ") = " + str(factorial(n)))
