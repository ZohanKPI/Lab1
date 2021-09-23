def EBNF_SyntaxChecker(string):
    if not string:
        return False, None
    elif string.isdigit():
        return True, int(string)

    flag = True
    subtract = False
    operationResult = 0

    for i in range(0, len(string), 2):
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
                operationResult += int(string[i]) if not subtract else -int(string[i])
        if string[i] not in "+-":
           flag = False
           break
    else:
        if not (string[i] == "+"):
           subtract = True
    if not flag:
        return False, None
    return True, operationResult
if __name__ == '__main__':
    string = input()
    print(EBNF_SyntaxChecker(string))