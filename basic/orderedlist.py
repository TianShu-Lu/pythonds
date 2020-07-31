from basic.unorderedlist import Node


class Orderedlist:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def add(self, item):
        current = self.head
        previous = None
        stop = False

        while current != None and not stop:  # 找到第一个比item大的位置
            if current.getData() > item:
                stop = True
            else:
                previous = current
                current = current.getNext()

        temp = Node(item)
        if previous == None:  # 插入在表头
            temp.setNext(self.head)
            self.head = temp
        else:  # 插入在表中的位置
            temp.setNext(current)
            previous.setNext(temp)

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
        stop = False

        while (current != None) and (not found) and (not stop):  # 当当前数据已经大于item，则后面的一定大于item
            if current.getData() == item:
                found = True
            else:
                if current.getData() > item:
                    stop = True
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
