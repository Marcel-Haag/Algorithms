def isDigit(z: str):
    if z == ")": return False
    if z == "(": return False
    if z == "*": return False
    if z == "+": return False
    if z == "-": return False
    if z == ":": return False
    return True


def isOperator(z: str):
    if z == "*": return True
    if z == "+": return True
    if z == "-": return True
    if z == ":": return True
    return False


def transformSuffix(expression: str):
    P = ""
    z = ""
    Stack = []

    while len(expression) > 0:
        z = expression[0]
        expression = expression[1:len(expression)]
        print("z=" + z + " expression=" + expression + " Stack=" + str(Stack) + " P=" + P)

        if isDigit(z): P = P + z
        if isOperator(z): Stack.append(z)
        if z == ")" and len(Stack) > 0: P = P + Stack.pop()

    print("z=" + z + " expression=" + expression + " Stack=" + str(Stack) + " P=" + P)
    while len(Stack) > 0:
        P = P + Stack.pop()
    return P


e = "(2+6)*7"
print("The reversed, polish notation of " + e + " is " + transformSuffix(e))
