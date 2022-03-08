# Greatest common divisor
def gcd(x: float, y: float):
    if y == 0:
        return x
    else:
        return gcd(y, x % y)


x = 5
y = 12
print("The greatest common divisor of " + str(x) + " and " + str(y) + " is " + str(gcd(x, y)))
