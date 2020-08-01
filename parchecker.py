from basic.stack import Stack


def parChecker(string):
    s = Stack()
    index = 0
    balance = True

    while index < len(string) and balance:
        symbol = string[index]
        if symbol in "{[(":
            s.push(symbol)
        else:
            if s.isEmpty():
                balance = True
            else:
                top = s.pop()
                if not match(top, symbol):
                    balance = False
        index = index + 1

    if balance and s.isEmpty():
        return True
    else:
        return False


def match(a, b):
    opens = "{[("
    closes = "}])"
    return opens.index(a) == closes.index(b)


if __name__ == "__main__":
    print(parChecker("{{[]}}"))
    print(parChecker("[[][{{"))
