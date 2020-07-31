class Node:  # 链式结构实现无序表最重要的基本元素：节点，包含数据信息以及下一个节点的引用信息
    def __init__(self, initdata):
        self.data = initdata
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self, newdata):
        self.data = newdata

    def setNext(self, newnext):
        self.next = newnext


class Unorderedlist:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def add(self, item):
        temp = Node(item)
        temp.setNext(self.head)  # 链接次序很重要！！先temp指向下一个，再把表头指向temp
        self.head = temp

    def size(self):  # 遍历每一个节点计数
        current = self.head
        count = 0

        while current != None:
            count = count + 1
            current = current.getNext()

        return count

    def search(self, item):  # 遍历每个节点进行比较
        current = self.head
        found = False

        while (current != None) and (not found):
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()

        return found

    def remove(self, item):
        current = self.head
        found = False
        previous = None

        while (current != None) and (not found):
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()

        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())

