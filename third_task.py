def EBNF_SyntaxChecker(string):
    result = tuple()
    if len(string) == 0:
        result = (False, None)
        return result
    elif string.isdigit():
        result = (True, int(string))
        return result
    flag = True
    subtract = False
    operationResult = 0
    for i in range(len(string)):
        if i % 2 == 0:
            if not string[i].isdigit():
                flag = False
                break
            else:
                if i == 0:
                    operationResult = int(string[i])
                else:
                    if subtract == False:
                        operationResult += int(string[i])
                    else:
                        operationResult -= int(string[i])
                        subtract = False
        else:
            if string[i] != "+" and string[i] != "-":
                flag = False
                break
            else:
                if string[i] == "+":
                    pass
                else:
                    subtract = True
    if flag == False:
        result = (False, None)

        return result
    else:
        result = (True, operationResult)
        return result
if __name__ == '__main__':
    string = input()
    print(EBNF_SyntaxChecker(string))



