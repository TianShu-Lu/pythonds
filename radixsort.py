from basic.queue import Queue

'''
思路是保持10个队列(队列0、队列1......队列9、队列main)，开始，所有的数都在main队列，没有排序。
第一趟将所有的数根据其10进制个位(0~9)，放入相应的队列0~9，全放好后，按照FIFO的顺序，将每个队列的数合并排到main队列。
第二趟再从main队列队首取数，根据其十位的数值，放入相应队列0~9，全放好后，仍然按照FIFO的顺序，将每个队列的数合并排到main队列。
第三趟放百位，再合并；第四趟放千位，再合并。
'''


def RadixSort(mainlist):
    nummax = max(mainlist)
    n = len(str(nummax))  # nummax的位数确定需要循环排位的次数
    mainqueue = [Queue(), Queue(), Queue(), Queue(), Queue(), Queue(), Queue(), Queue(), Queue(), Queue()]  # 创建十个队列

    for i in range(n):
        while mainlist:
            num = mainlist.pop(0)
            digit = num // (10**i) % 10  # 取出相应的位数
            mainqueue[digit].enqueue(num)
        for bucket in mainqueue:
            while not bucket.isEmpty():
                mainlist.append(bucket.dequeue())

    return mainlist


if __name__ == '__main__':
    mylist = eval(input())
    print(RadixSort(mylist))
