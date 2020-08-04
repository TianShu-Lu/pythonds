from basic.stack import Stack


# 一维字符串的消消乐
def xiaoxiaole(strings):
    s = Stack()
    list = []

    for str in strings:  # 如果与栈顶相同则消去栈顶， 不同则压入栈顶
        if str == s.peek():
            s.remove()
        else:
            s.push(str)

    if s.isEmpty():
        return None
    else:
        while not s.isEmpty():
            list.insert(0, s.pop())  # 取出栈中的每个元素，注意排列顺序
        return "".join(list)


if __name__ == "__main__":
    print(xiaoxiaole("beepooxxxyz"))
    print(xiaoxiaole("abbacddccc00"))

