from basic.stack import Stack

'''
本题有几个默认条件（一开始想多了非常懵逼但其实很简单）
1.默认一轮只用10个盘子且全部用完（不存在顾客用完又还回来）
2.默认洗碗工一轮开始时，有10个盘子待洗
3
所以解题思路为：从startstring中当前取出的盘子编号若大于前一个，OK；若小于前一个，
判断是不是离前一个盘子编号最近的那一个，若是，OK，不是，洗碗工就被抓住偷懒了
'''


def Dishwasher(startstring):
    startlist = [int(i) for i in startstring]
    found = True
    plants = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]  # 每一轮开始时，有十个盘子，拿走一个，对应编号处变为None

    for i in range(9):
        plants[startlist[i]] = None
        front = startlist[i]
        behind = startlist[i + 1]
        if behind < front:
            while behind != front - 1 and found:  # 如果behind小于front，并且不等于最近的剩余盘子，则偷懒
                if plants[front - 1] == None:
                    front = front - 1
                else:
                    found = False

    if found:
        return "Yes"
    else:
        return "No"


if __name__ == "__main__":
    print(Dishwasher("1043257689"))
    print(Dishwasher("4230178956"))
