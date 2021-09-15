def MathCalculation(string)
    resultOfOperation = 0
    if string[0].lower() == "add":
        resultOfOperation = int(string[1]) + int(string[2])
    elif string[0].lower() == "subtract":
        resultOfOperation = int(string[1]) - int(string[2])
    elif string[0].lower() == "multiply":
        resultOfOperation = int(string[1]) * int(string[2])
    elif string[0].lower() == "divide":
        resultOfOperation = int(string[1]) / int(string[2])
    else:
        return None
    return resultOfOperation
if __name__ == '__main__':
    string = input()
    string = string.split()
    print(MathCalculation(string))



