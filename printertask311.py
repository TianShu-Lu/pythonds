from basic.queue import Queue
import random


class Printer:  # 打印机对象
    def __init__(self, ppm):
        self.pagerate = ppm  # 打印速度
        self.currenttask = None  # 当前打印状态
        self.timeRemaining = 0  # 当前任务结束倒计时

    def trick(self):  # 模拟时间流逝一秒 打印机所做的事
        if self.currenttask is not None:
            self.timeRemaining = self.timeRemaining - 1
            if self.timeRemaining <= 0:
                self.currenttask = None

    def busy(self):  # 判断打印机是否正在打印
        if self.currenttask is not None:
            return True
        else:
            return False

    def startNext(self, newtask):  # 开始下一个新任务
        self.currenttask = newtask
        self.timeRemaining = newtask.getPages() / (self.pagerate / 60)


class Task:  # 建立打印任务对象
    def __init__(self, time):
        self.timestamp = time  # 建立打印任务开始时的时间戳
        self.pages = random.randrange(1, 21)  # 生成打印任务的页数，为随机的1~20

    def getStamp(self):
        return self.timestamp

    def getPages(self):
        return self.pages

    def waittime(self, currenttime):  # 返回该任务等待打印的排队时间
        return currenttime - self.timestamp


def newPrinttask():
    num = random.randrange(1, 181)  # 1/180的概率有新任务生成
    if num == 180:
        return True
    else:
        return False


def simulation(numseconds, pagesperminutes):  # 模拟时间流逝，传入运行多长时间和打印速度
    printer = Printer(pagesperminutes)
    printQueue = Queue()  # 生成打印队列
    waitingtimes = []  # 用来记录所有打印任务的等待时间

    for currentsecond in range(numseconds):
        if newPrinttask():
            printQueue.enqueue(Task(currentsecond))

        if (not printer.busy()) and (not printQueue.isEmpty()):
            newTask = printQueue.dequeue()
            printer.startNext(newTask)
            waitingtimes.append(newTask.waittime(currentsecond))

        printer.trick()

    averageWait = sum(waitingtimes) / len(waitingtimes)
    print("Average Wait %6.2f secs %3d tasks remaining." % (averageWait, printQueue.size()))


if __name__ == '__main__':
    for i in range(10):
        simulation(3600, 5)
