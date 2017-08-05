#Takes the user's input and splits each number and symbol into its own spot on the array. Takes into account negative numbers, fractions, and exponents
def makeArray(input):
    arry = []
    placeholder = ""
    for x in range(0, len(input)):
        if input[x] != " " and x != len(input) - 1 and input[x] != "(" and input[x] != ")":
            if input[x] == "-" and isNumber(input[x + 1]):
                placeholder += input[x:x + 1]
            else:
                placeholder += input[x]
        elif input[x] == "(":
            arry.append(input[x])
        elif input[x] == ")" and len(placeholder) > 0:
            arry.append(placeholder)
            arry.append(input[x])
            placeholder = ""
        elif x == len(input) - 1:
            placeholder += input[x]
            arry.append(placeholder)
        elif len(placeholder) > 0:
            arry.append(placeholder)
            placeholder = ""
    return arry

#trys to convert the input to a float, which throws an error unless it's a number. Used to find if the next value in the original string is a space or number(as in -7)
#I imagine there is a better way to do this since I'm not really using try how its intended
def isNumber(num):
    try:
        float(num)
    except:
        return False
    return True

#For character in the string, finds any string with / that is not a division sign, then evaluates the fraction
def evaluateFraction(num):
    numer = 0
    denum = 0
    for x in range(len(num)):
        if num[x] == "/" and x > 0:
            numer = num[0:x]
            denum = num[x + 1: len(num)]
            return str(float(numer) / float(denum))
    return num

#Goes through the array and sends the value of each index into the evaluatefraction function
def findFractions(arry):
    for i in range(len(arry)):
        arry[i] = evaluateFraction(arry[i])

#works the same way as evaluatefraction for exponents
def evaluateExponents(num):
    numb = 0
    exp = 0
    for x in range(len(num)):
        if num[x] == "^":
            numb = num[0:x]
            exp = num[x + 1: len(num)]
            return str(pow(int(numb), int(exp)))
    return num

#again, like findfractions
def findExponents(arry):
    for i in range(len(arry)):
        arry[i] = evaluateExponents(arry[i])

#Called after solving fractions/exponents, so it does not have to worry about extrannious symbols. Also called after dealing with parenthesis, so it does not have to deal with that. Finds the multiply/divide signs and gets the numbers from each side, solves, and removes two slots on the array and replaces the third with the answer
def multDiv(arry):
    for i in range(len(arry)):
        if arry[i] == "/":
            arry[i] = str(float(arry[i - 1]) / float(arry[i + 1]))
            print(arry)
            del arry[i - 1]
            print(arry)
            del arry[i]
            print(arry)
            return multDiv(arry)
        if arry[i] == "*":
            arry[i] = str(float(arry[i - 1]) * float(arry[i + 1]))
            print(arry)
            del arry[i - 1]
            print(arry)
            del arry[i]
            print(arry)
            return multDiv(arry)
    return arry

#Functions the exact same way as multiply/divide, but has to a seperate function to comply with order of operations
def addSub(arry):
    for i in range(len(arry)):
        if arry[i] == "+":
            arry[i] = str(float(arry[i - 1]) + float(arry[i + 1]))
            print(arry)
            del arry[i - 1]
            print(arry)
            del arry[i]
            print(arry)
            return addSub(arry)
        if arry[i] == "-":
            arry[i] = str(float(arry[i - 1]) - float(arry[i + 1]))
            print(arry)
            del arry[i - 1]
            print(arry)
            del arry[i]
            print(arry)
            return addSub(arry)
    return arry

#Used to get to the most nested of the first ), makes a new array and appends to the array the input past the outermost (, then recurses to get to the most nested.
def parenHelper(arry):
    newarry = []
    for x in range(len(arry) - 1):
        if arry[x] == "(":
            start = x
            for i in range(start + 1, len(arry)):
                newarry.append(arry[i])
            newarry = parenHelper(newarry)
            return newarry
    return arry

#creats a arry then appends the from the first ( to the first ) of the original array
def findParen2(arry):
    newarry = []
    for x in range(len(arry)):
        if arry[x] == "(":
            start = x
            for i in range(len(arry)):
                if arry[i] == ")":
                    stop = i
                    break
            for n in range(start + 1, stop):
                newarry.append(arry[n])
            newarry = parenHelper(newarry)
            return newarry
    return arry

#Uses the inner of the deepest parenthesis found by findParen2, and runs solves.
def evaluateParenthesis(arry):
    found = findParen2(arry)
    multDiv(found)
    addSub(found)
    return found

#Finds the first closing parenthesis, then finds the opening parenthesis that corresponds to it in order to find the deepest nested parenthesis in the array. Also finds the index of the parenthesis deletes all but the closing parenthesis. Then, it replaces the closing parenthesis with the solved inner parenthesis and recurses in order to solve a possible outer parenthesis (7 + (8 * 2))
def replaceParen2(arry, newarry):
    for x in range(len(arry)):
        if arry[x] == ")":
            start = x
            for i in range(x, -1, -1):
                if arry[i] == "(":
                    stop = i
                    for n in range(stop, start):
                        del arry[stop]
                        print(arry)
                    for r in range(len(arry)):
                        if arry[r] == ")":
                            arry[r] = float(newarry[0])
                            print(arry)
                            arry = replaceParen2(arry, evaluateParenthesis(arry))
                            return arry
    return arry

#Uses all the above functions to first, convert the input string into a useable array, evaluate fractions and exponents, solving parenthesis, then solving the problem with the solutions of the parenthesis substituted in.
def solve(strarry):
    arry = makeArray(strarry)
    findFractions(arry)
    findExponents(arry)
    arry = replaceParen2(arry, evaluateParenthesis(arry))
    return arry

arry = "((4 - -3) + 8)"
solve(arry)
