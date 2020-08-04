class Stack:
    def __init__(self):
        self.items = list()

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        if not self.items:
            return None
        else:
            return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)

    def remove(self):  # 移除栈顶数据
        del self.items[len(self.items)-1]

