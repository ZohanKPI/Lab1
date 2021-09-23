def EBNF_SyntaxChecker(string):
    result = tuple()
    if not string:
        return False, None
    elif string.isdigit():
        return True, int(string)
    flag = True
    subtract = False
    operationResult = 0
    for i in range(len(string)):
        if not i % 2:
            if not string[i].isdigit():
                flag = False
                break
            if not (string[i+1].isdigit()):
                flag = False
                break
            else:
                if not i:
                    operationResult = int(string[i])
                else:
                    if subtract == False:
                        operationResult += int(string[i])
                    else:
                        operationResult -= int(string[i])
        else:
            if string[i] not in "+-":
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