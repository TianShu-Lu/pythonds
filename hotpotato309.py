from basic.queue import Queue


def hotPotato(namelist, num):
    simqueue = Queue()
    for name in namelist:
        simqueue.enqueue(name)  # 把所有人名压入队列

    while simqueue.size() > 1:
        for i in range(num):
            simqueue.enqueue(simqueue.dequeue())  # 循环num次，把首端人名压入尾端
        simqueue.dequeue()  # 然后确定该次循环中谁出列

    return simqueue.dequeue()


if __name__ == "__main__":
    print(hotPotato(["Bill", "Jack", "Tom", "Cathy"], 3))
