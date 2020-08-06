from basic.queue import Queue


def reqNum(mylist):
    q = Queue()
    mylist.sort()  # 各个请求时间排序
    num = []  # 用来存放请求次数

    for i in mylist:
        q.enqueue(i)
        while i - q.peekfront() > 10000:  # 队首的请求时间一定是最早的，判断与当前请求时间的差值，大于10000，则删除队首
            q.remove()
        num.append(q.size())  #此时队列中的元素个数即为在10000毫秒内的请求次数

    return num


if __name__ == "__main__":
    mylist = eval(input())
    print(reqNum(mylist))
