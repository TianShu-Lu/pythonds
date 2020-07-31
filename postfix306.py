from basic.stack import Stack


def infixTopostfix(infix):
    prec = {"*": 3, "/": 3, "+": 2, "-": 2, "(": 1, ")": 1}

    opstack = Stack()
    postfixlist = []
    infixlist = infix.split()

    for token in infixlist:
        if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in "0123456789":
            postfixlist.append(token)
        elif token == "(":
            opstack.push(token)
        elif token == ")":
            toptoken = opstack.pop()
            while toptoken != "(":
                postfixlist.append(toptoken)
                toptoken = opstack.pop()
        else:
            while (not opstack.isEmpty()) and prec[opstack.peek()] >= prec[token]:
                postfixlist.append(opstack.pop())
            opstack.push(token)

    while not opstack.isEmpty():
        postfixlist.append(opstack.pop())

    return " ".join(postfixlist)


if __name__ == "__main__":
    print(infixTopostfix("( A + B ) * C"))

