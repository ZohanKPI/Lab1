from sys import argv
def MathCalculation(string):
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
try:
    if __name__ == '__main__':
        string = argv[1:]
        print(MathCalculation(string))
    MathCalculation(string)
except ValueError:
    print('Invalid Input')
except ZeroDivisionError:
    print('Divided by zero')

