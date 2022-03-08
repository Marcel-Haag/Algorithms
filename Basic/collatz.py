# For a natural number the return value will be always be 1
# There is no known number where the Collatz Algorithm won't terminate
def collatz(number: int):
    while number != 1:
        if number % 2 == 1:
            number = 3 * number + 1
        number = number / 2
    return number


n = 13
# S(13) = S(40) = S(20) = S(10) = S(5) = S(16) = S(8) = S(4) = S(2) = S(1) = 1
print("Die Collatz-Funktion von " + str(n) + " = " + str(collatz(n)))
