def MathCalculation(string):
    resultOfOperation = 0
    if string[1] == "+":
        resultOfOperation = int(string[0]) + int(string[2])
    elif string[1] == "-":
        resultOfOperation = int(string[0]) - int(string[2])
    elif string[1] == "*":
        resultOfOperation = int(string[0]) * int(string[2])
    elif string[1] == "/":
        resultOfOperation = int(string[0]) / int(string[2])
    else:
        return None
    return resultOfOperation
if __name__ == '__main__':
    string = input()
    string = string.split()
    print(MathCalculation(string))



